from ScoutSuite.providers.gcp.facade.gcp import GCPFacade
from ScoutSuite.providers.gcp.resources.projects import Projects
from ScoutSuite.providers.gcp.resources.cloudresourcemanager.bindings import Bindings

class CloudResourceManager(Projects):
    _children = [  
        (Bindings, 'bindings') 
    ]

    def __init__(self, gcp_facade: GCPFacade):
        super(CloudResourceManager, self).__init__(gcp_facade)

