
import boto3
client = boto3.client('emr')

response = client.add_instance_fleet(
    ClusterId='string',
    InstanceFleet={
        'Name': 'string',
        'InstanceFleetType': 'MASTER'|'CORE'|'TASK',
        'TargetOnDemandCapacity': 123,
        'TargetSpotCapacity': 123,
        'InstanceTypeConfigs': [
            {
                'InstanceType': 'string',
                'WeightedCapacity': 123,
                'BidPrice': 'string',
                'BidPriceAsPercentageOfOnDemandPrice': 123.0,
                'EbsConfiguration': {
                    'EbsBlockDeviceConfigs': [
                        {
                            'VolumeSpecification': {
                                'VolumeType': 'string',
                                'Iops': 123,
                                'SizeInGB': 123
                            },
                            'VolumesPerInstance': 123
                        },
                    ],
                    'EbsOptimized': True|False
                },
                'Configurations': [
                    {
                        'Classification': 'string',
                        'Configurations': {'... recursive ...'},
                        'Properties': {
                            'string': 'string'
                        }
                    },
                ],
                'CustomAmiId': 'string'
            },
        ],
        'LaunchSpecifications': {
            'SpotSpecification': {
                'TimeoutDurationMinutes': 123,
                'TimeoutAction': 'SWITCH_TO_ON_DEMAND'|'TERMINATE_CLUSTER',
                'BlockDurationMinutes': 123,
                'AllocationStrategy': 'capacity-optimized'
            },
            'OnDemandSpecification': {
                'AllocationStrategy': 'lowest-price',
                'CapacityReservationOptions': {
                    'UsageStrategy': 'use-capacity-reservations-first',
                    'CapacityReservationPreference': 'open'|'none',
                    'CapacityReservationResourceGroupArn': 'string'
                }
            }
        }
    }
)