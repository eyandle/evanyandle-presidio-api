from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from .AWSModels import CiscoToAws
from .ParseCiscoConfig import parse_cisco_configuration
from .MakeAWSCFT import create_cft_file
AWSRouter = APIRouter()


@AWSRouter.post('/cisco_to_aws')
def cisco_to_aws(data: CiscoToAws):
    if not data.iface_config:
        raise HTTPException(400, 'iface_config is Required')

    subnets = parse_cisco_configuration(data.iface_config)
    cft = create_cft_file(subnets)

    return StreamingResponse(cft,
                             media_type="text/json",
                             headers={'Content-Disposition': 'filename=CFT.json'})
