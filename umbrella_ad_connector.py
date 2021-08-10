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
    name = "umbrellava_adconnector",
    detect = startswith(".1.3.6.1.2.1.1.2.0", ".1.3.6.1.4.1.8072.3.2.10"),
    fetch=SNMPTree(
            base=".1.3.6.1.4.1.8072.1.3.2.4.1.2.2.97.100",
            oids=[
                '1', # ADConnectorState
                '2', # ADConnectorLastEventDate
            ])
)
def check_umbrellava_adconnector(item, section):
    for ADConnectorState, ADConnectorLastEventDate in section:
      #print(ADConnectorState)
      if "green" in ADConnectorState:
        state = State.OK
      elif "yellow" in ADConnectorState:
        state = State.WARN
      else:
        state = State.CRIT 
      yield Result(
          state = state,
          summary = ((ADConnectorState.split(':')[-1])+ ' - ' + ADConnectorLastEventDate))
      return



def discover_umbrellava_adconnector(section):
    for ADConnectorState, ADConnectorLastEventDate in section: 
      #print(ADConnectorState)
      servicename = ADConnectorState[ADConnectorState.find(':')+len(':'):ADConnectorState.rfind(':')]
      yield Service(item=servicename)

register.check_plugin(
    name = "umbrellava_adconnector",
    service_name = "UmbrellaVA %s",
    discovery_function = discover_umbrellava_adconnector,
    check_function = check_umbrellava_adconnector,
)
