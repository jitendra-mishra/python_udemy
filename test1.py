steps = [
    {
        "name": "populate_data_for_pitr_1",
        "method": "self.populate_data_for_pitr",
        "input": {"database_name": "self.database_name"}
    },
    {
        "name": "populate_data_for_pitr_2",
        "method": "self.populate_data_for_pitr",
        "input": {"sqlcmds_list_index": [1],
                  "database_name": "self.database_name"},
        "depend": ["populate_data_for_pitr_1"]
    },
    {
        "name": "perform_database_restore",
        "method": "self.application_object.database_restore",
        "input": {
            "uuid": "self.application_object.database_id",
            "pitr": "$populate_data_for_pitr_1",
            "max_recovery": False
        },
        "depend": ["populate_data_for_pitr_2"]
    },
    {
        "name": "validate_database_restore",
        "method": "self.validate_database_restore",
        "input": {'database_name': "self.database_name"},
        "depend": ["perform_database_restore", "wait_for_heal_snapshot"]
    }
]

db_type = "postgres"
if db_type == "postgres":
    heal_snapshot_depends_on = "populate_data_for_pitr_2"
else:
    heal_snapshot_depends_on = "perform_database_restore"
print(f"Heal={heal_snapshot_depends_on}")
restore_step = [{
    "name": "wait_for_heal_snapshot",
    "method": "self.timemachine_object.wait_for_heal_snapshot",
    "input": {
        'timemachine_id': "self.application_object.timemachine_id"
    },
    "depend": ['heal_snapshot_depends_on']
}
]
print(len(steps))
print(restore_step)
steps.append(restore_step)
print(len(steps))
