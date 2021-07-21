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
    name = "umbrellava_clouddns",
    detect = startswith(".1.3.6.1.2.1.1.2.0", ".1.3.6.1.4.1.8072.3.2.10"),
    #parse_function=parse_acgateway_alarms,
    fetch=SNMPTree(
            base=".1.3.6.1.4.1.8072.1.3.2.4.1.2.3.100.110.115",
            oids=[
                '1', # UmbrellaDNSConnectionState
                '2', # UmbrellaResolver2UDPlookup
                '3', # UmbrellaResolver2TCPlookup
                '4', # UmbrellaResolver1UDPlookup
                '5', # UmbrellaResolver1TCPlookup
])
)
def check_umbrellava_clouddns(item, section):
    for UmbrellaDNSConnectionState, UmbrellaResolver2UDPlookup,UmbrellaResolver2TCPlookup,UmbrellaResolver1UDPlookup, UmbrellaResolver1TCPlookup in section:
      #print(ADConnectorState)
      if "green" in UmbrellaDNSConnectionState:
        state = State.OK
      elif "yellow" in UmbrellaDNSConnectionState:
        state = State.WARN
      else:
        state = State.CRIT
      summary = (UmbrellaDNSConnectionState.split(':')[-1])
      outputlist = [UmbrellaResolver2UDPlookup,UmbrellaResolver2TCPlookup,UmbrellaResolver1UDPlookup, UmbrellaResolver1TCPlookup]
      for listitem in outputlist:
        if listitem:
          summary += ("," + listitem)
      yield Result(
          state = state,
          summary = summary)
      return



def discover_umbrellava_clouddns(section):
    for UmbrellaDNSConnectionState, UmbrellaResolver2UDPlookup,UmbrellaResolver2TCPlookup,UmbrellaResolver1UDPlookup, UmbrellaResolver1TCPlookup in section:
      #print(ADConnectorState)
      servicename = UmbrellaDNSConnectionState[UmbrellaDNSConnectionState.find(':')+len(':'):UmbrellaDNSConnectionState.rfind(':')]
      yield Service(item=servicename)

register.check_plugin(
    name = "umbrellava_clouddns",
    service_name = "UmbrellaVA %s",
    discovery_function = discover_umbrellava_clouddns,
    check_function = check_umbrellava_clouddns,
    #check_default_parameters = {"warning_lower": 10},
    #check_ruleset_name = "foobar",
)
