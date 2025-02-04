from collections import OrderedDict
from typing import Dict, List, Type, Union

from bitca.aws.resource.acm.certificate import AcmCertificate
from bitca.aws.resource.base import AwsResource
from bitca.aws.resource.cloudformation.stack import CloudFormationStack
from bitca.aws.resource.ec2.security_group import SecurityGroup
from bitca.aws.resource.ec2.subnet import Subnet
from bitca.aws.resource.ec2.volume import EbsVolume
from bitca.aws.resource.ecs.cluster import EcsCluster
from bitca.aws.resource.ecs.service import EcsService
from bitca.aws.resource.ecs.task_definition import EcsTaskDefinition
from bitca.aws.resource.elasticache.cluster import CacheCluster
from bitca.aws.resource.elasticache.subnet_group import CacheSubnetGroup
from bitca.aws.resource.elb.listener import Listener
from bitca.aws.resource.elb.load_balancer import LoadBalancer
from bitca.aws.resource.elb.target_group import TargetGroup
from bitca.aws.resource.emr.cluster import EmrCluster
from bitca.aws.resource.glue.crawler import GlueCrawler
from bitca.aws.resource.iam.policy import IamPolicy
from bitca.aws.resource.iam.role import IamRole
from bitca.aws.resource.rds.db_cluster import DbCluster
from bitca.aws.resource.rds.db_instance import DbInstance
from bitca.aws.resource.rds.db_subnet_group import DbSubnetGroup
from bitca.aws.resource.s3.bucket import S3Bucket
from bitca.aws.resource.secret.manager import SecretsManager

# Use this as a type for an object which can hold any AwsResource
AwsResourceType = Union[
    AcmCertificate,
    CloudFormationStack,
    EbsVolume,
    IamRole,
    IamPolicy,
    GlueCrawler,
    S3Bucket,
    SecretsManager,
    Subnet,
    SecurityGroup,
    DbSubnetGroup,
    DbCluster,
    DbInstance,
    CacheSubnetGroup,
    CacheCluster,
    EmrCluster,
    EcsCluster,
    EcsTaskDefinition,
    EcsService,
    LoadBalancer,
    TargetGroup,
    Listener,
]

# Use this as an ordered list to iterate over all AwsResource Classes
# This list is the order in which resources should be installed as well.
AwsResourceTypeList: List[Type[AwsResource]] = [
    Subnet,
    SecurityGroup,
    IamRole,
    IamPolicy,
    S3Bucket,
    SecretsManager,
    EbsVolume,
    AcmCertificate,
    CloudFormationStack,
    GlueCrawler,
    DbSubnetGroup,
    DbCluster,
    DbInstance,
    CacheSubnetGroup,
    CacheCluster,
    LoadBalancer,
    TargetGroup,
    Listener,
    EcsCluster,
    EcsTaskDefinition,
    EcsService,
    EmrCluster,
]

# Map Aws resource alias' to their type
_aws_resource_type_names: Dict[str, Type[AwsResource]] = {
    aws_type.__name__.lower(): aws_type for aws_type in AwsResourceTypeList
}
_aws_resource_type_aliases: Dict[str, Type[AwsResource]] = {
    "s3": S3Bucket,
    "volume": EbsVolume,
}

AwsResourceAliasToTypeMap: Dict[str, Type[AwsResource]] = dict(**_aws_resource_type_names, **_aws_resource_type_aliases)

# Maps each AwsResource to an install weight
# lower weight AwsResource(s) get installed first
AwsResourceInstallOrder: Dict[str, int] = OrderedDict(
    {resource_type.__name__: idx for idx, resource_type in enumerate(AwsResourceTypeList, start=1)}
)
