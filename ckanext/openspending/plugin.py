import ckan.plugins as plugins

import datetime
import dateutil.parser
import os.path
import json
import urlparse
import requests

from budgetdatapackage import BudgetDataPackage, BudgetResource
from ckanext.openspending import exceptions

import logging
log = logging.getLogger(__name__)


class OpenSpendingPlugin(plugins.SingletonPlugin):
    """OpenSpending data submission

    The plugin models and loads a resource which complies to the budget data
    package specification. The data is loaded via a single OpenSpending user
    retrieved from the API key in the configuration file.
    """

    plugins.implements(plugins.IConfigurable)
    plugins.implements(plugins.IResourceController)

    def __init__(self, *args, **kwargs):
        self.openspending = {}
        self.data = None

    def configure(self, config):
        """
        Initialize the plugin. This creates a data object which holds a
        BudgetDataPackage parser which operates based on a specification
        which is either provided in the config via:
        ``ckan.budgets.specification`` or the included version.
        """

        self.openspending['url'] = config.get(
            'openspending.url',
            'https://openspending.org/')

        self.openspending['apikey'] = config.get(
            'openspending.apikey',
            None)

        if self.openspending['apikey'] is None:
            raise exceptions.OpenSpendingException(
                'OpenSpending API Key not configured')

        self.openspending['ckan_url'] = config.get(
            'ckan.site_url',
            None)

        if self.openspending['ckan_url'] is None:
            raise exceptions.OpenSpendingException(
                'OpenSpending extension requires ckan.site_url to be set')

    def before_create(self, context, resource):
        pass

    def after_create(self, context, resource):
        """
        Submits the newly created resource to OpenSpending
        """

        if not resource.get('BudgetDataPackage', False):
            return
        
        resource_url = plugins.toolkit.url_for(
            controller='package',
            action='resource_read',
            id=context['package'].name,
            resource_id=resource['id'])
        resource_url = urlparse.urljoin(
            self.openspending['ckan_url'], resource_url)

        if resource_url[-1] != '/':
            resource_url += '/'

        parameters = {'budget_data_package': resource_url}
        headers = {
            'Authorization': 'ApiKey {key}'.format(
                key=self.openspending['apikey'])
        }

        openspending_url = urlparse.urljoin(
            self.openspending['url'], '/api/2/new')
        response = requests.post(
            openspending_url, params=parameters, headers=headers)
        log.debug('Submitted budget data package {url}: {code}'.format(
            url=resource_url, code=response.status_code))

    def before_update(self, context, current, resource):
        pass

    def after_update(self, context, resource):
        """
        Deletes the existing resource and resubmits it to OpenSpending.
        This must be done because currently OpenSpending does not support
        in-place updating datasets which could happen.
        """
        pass

    def before_delete(self, context, resource, resources):
        """
        Deletes the existing resource on OpenSpending.
        """
        pass

    def after_delete(self, context, resources):
        pass

    def before_show(self, resource):
        return resource
