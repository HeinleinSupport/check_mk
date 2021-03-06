#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

multisite_builtin_views.update({
    'aggr_all_api': {'browser_reload': 0,
                  'column_headers': 'pergroup',
                  'context': {'aggr_name_regex': {'aggr_name_regex': ''}},
                  'datasource': 'bi_aggregations',
                  'description': u'List of all aggregations, containing the name of aggregations and state information\n',
                  'force_checkboxes': False,
                  'group_painters': [],
                  'hidden': True,
                  'hidebutton': True,
                  'icon': 'aggr',
                  'layout': 'table',
                  'linktitle': u'All Aggregations',
                  'mobile': False,
                  'mustsearch': False,
                  'name': 'aggr_all_api',
                  'num_columns': 1,
                  'painters': [('aggr_group', None, None),
                               ('aggr_name', None, None),
                               ('aggr_state_num', None, None),
                               ('aggr_output', None, None),
                               ('aggr_treestate', None, None),
                               ('aggr_in_downtime', None, None),
                               ('aggr_acknowledged', None, None)],
                  'play_sounds': False,
                  'public': True,
                  'single_infos': [],
                  'sorters': [],
                  'title': u'List of all Aggregations for simple API calls',
                  'topic': u'Business Intelligence',
                  'user_sortable': False}})
