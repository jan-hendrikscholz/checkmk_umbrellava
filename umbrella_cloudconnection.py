from .agent_based_api.v1 import (
    contains,
    startswith,
    register,
    render,
    Metric,
    OIDEnd,
    Result,
    Service,
    SNMPTree,
    State,
)

register.snmp_section(
    name = "umbrellava_cloudconnection",
    detect = startswith(".1.3.6.1.2.1.1.2.0", ".1.3.6.1.4.1.8072.3.2.10"),
    fetch=SNMPTree(
            base=".1.3.6.1.4.1.8072.1.3.2.4.1.2.5.99.108.111.117.100",
            oids=[
                '1', # UmbrellaCloudConnectionState
                '2', # UmbrellaCloudSSLState
            ]),
)
def check_umbrellava_cloudconnection(item, section):
    for UmbrellaCloudConnectionState, UmbrellaCloudSSLState in section:
      if "green" in UmbrellaCloudConnectionState:
        state = State.OK
      elif "yellow" in UmbrellaCloudConnectionState:
        state = State.WARN
      else:
        state = State.CRIT 
      yield Result(
          state = state,
          summary = ((UmbrellaCloudConnectionState.split(':')[-1])+ ' - ' + UmbrellaCloudSSLState))
      return



def discover_umbrellava_cloudconnection(section):
    for UmbrellaCloudConnectionState, UmbrellaCloudSSLState in section:
      servicename = UmbrellaCloudConnectionState[UmbrellaCloudConnectionState.find(':')+len(':'):UmbrellaCloudConnectionState.rfind(':')]
      yield Service(item=servicename)

register.check_plugin(
    name = "umbrellava_cloudconnection",
    service_name = "UmbrellaVA %s",
    discovery_function = discover_umbrellava_cloudconnection,
    check_function = check_umbrellava_cloudconnection,
    #check_default_parameters = {"warning_lower": 10},
    #check_ruleset_name = "foobar",
)
