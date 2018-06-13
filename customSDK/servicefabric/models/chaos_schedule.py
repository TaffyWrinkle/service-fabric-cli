# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChaosSchedule(Model):
    """Defines the schedule used by Chaos.

    :param start_date: The date and time Chaos will start using this schedule.
     . Default value: "1601-01-01T00:00:00Z" .
    :type start_date: datetime
    :param expiry_date: The date and time Chaos will continue to use this
     schedule until.
     . Default value: "9999-12-31T23:59:59.999Z" .
    :type expiry_date: datetime
    :param chaos_parameters_dictionary: A mapping of string names to Chaos
     Parameters to be referenced by Chaos Schedule Jobs.
    :type chaos_parameters_dictionary:
     list[~azure.servicefabric.models.ChaosParametersDictionaryItem]
    :param jobs: A list of all Chaos Schedule Jobs that will be automated by
     the schedule.
    :type jobs: list[~azure.servicefabric.models.ChaosScheduleJob]
    """

    _attribute_map = {
        'start_date': {'key': 'StartDate', 'type': 'iso-8601'},
        'expiry_date': {'key': 'ExpiryDate', 'type': 'iso-8601'},
        'chaos_parameters_dictionary': {'key': 'ChaosParametersDictionary', 'type': '[ChaosParametersDictionaryItem]'},
        'jobs': {'key': 'Jobs', 'type': '[ChaosScheduleJob]'},
    }

    def __init__(self, start_date="1601-01-01T00:00:00Z", expiry_date="9999-12-31T23:59:59.999Z", chaos_parameters_dictionary=None, jobs=None):
        super(ChaosSchedule, self).__init__()
        self.start_date = start_date
        self.expiry_date = expiry_date
        self.chaos_parameters_dictionary = chaos_parameters_dictionary
        self.jobs = jobs