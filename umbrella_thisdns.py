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
    name = "umbrellava_thisdns",
    detect = startswith(".1.3.6.1.2.1.1.2.0", ".1.3.6.1.4.1.8072.3.2.10"),
    fetch=SNMPTree(
            base=".1.3.6.1.4.1.8072.1.3.2.4.1.2.7.116.104.105.115.100.110.115",
            oids=[
                '1', # UmbrellaThisDNSState
                '2', # UmbrellaThisDNSTCPState
                '3', # UmbrellaThisDNSUDPState
            ]),
)
def check_umbrellava_thisdns(item, section):
    for UmbrellaThisDNSState, UmbrellaThisDNSTCPState,UmbrellaThisDNSUDPState in section:
      #print(ADConnectorState)
      if "green" in UmbrellaThisDNSState:
        state = State.OK
      elif "yellow" in UmbrellaThisDNSState:
        state = State.WARN
      else:
        state = State.CRIT
      summary = (UmbrellaThisDNSState.split(':')[-1])
      outputlist = [UmbrellaThisDNSTCPState,UmbrellaThisDNSUDPState]
      for listitem in outputlist:
        if listitem:
          summary += ("," + listitem)
      yield Result(
          state = state,
          summary = summary)
      return



def discover_umbrellava_thisdns(section):
    for UmbrellaThisDNSState, UmbrellaThisDNSTCPState,UmbrellaThisDNSUDPState in section:
      #print(ADConnectorState)
      servicename = UmbrellaThisDNSState[UmbrellaThisDNSState.find(':')+len(':'):UmbrellaThisDNSState.rfind(':')]
      yield Service(item=servicename)

register.check_plugin(
    name = "umbrellava_thisdns",
    service_name = "UmbrellaVA %s",
    discovery_function = discover_umbrellava_thisdns,
    check_function = check_umbrellava_thisdns,
    #check_default_parameters = {"warning_lower": 10},
    #check_ruleset_name = "foobar",
)
