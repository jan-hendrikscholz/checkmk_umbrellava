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
    name = "umbrellava_localdns",
    detect = startswith(".1.3.6.1.2.1.1.2.0", ".1.3.6.1.4.1.8072.3.2.10"),
    fetch=SNMPTree(
            base=".1.3.6.1.4.1.8072.1.3.2.4.1.2.8.108.111.99.97.108.100.110.115",
            oids=[
                '1', # UmbrellaLocalDNSState
                '2', # UmbrellaLocalDNS1UDPState
                '3', # UmbrellaLocalDNS1TCPState
                '4', # UmbrellaLocalDNS2UDPState
                '5', # UmbrellaLocalDNS2TCPState
                '6', # UmbrellaLocalDNS3UDPState
                '7', # UmbrellaLocalDNS3TCPState
            ])
)
def check_umbrellava_localdns(item, section):
    for UmbrellaLocalDNSState, UmbrellaLocalDNS1UDPState,UmbrellaLocalDNS1TCPState,UmbrellaLocalDNS2UDPState, UmbrellaLocalDNS2TCPState, UmbrellaLocalDNS3UDPState,UmbrellaLocalDNS3TCPState in section:
      #print(ADConnectorState)
      if "green" in UmbrellaLocalDNSState:
        state = State.OK
      elif "yellow" in ADConnectorState:
        state = State.WARN
      else:
        state = State.CRIT
      summary = (UmbrellaLocalDNSState.split(':')[-1])
      outputlist = [UmbrellaLocalDNS1UDPState,UmbrellaLocalDNS1TCPState,UmbrellaLocalDNS2UDPState, UmbrellaLocalDNS2TCPState, UmbrellaLocalDNS3UDPState,UmbrellaLocalDNS3TCPState]
      for listitem in outputlist:
        if listitem:
          summary += ("," + listitem)
      yield Result(
          state = state,
          summary = summary)
      return



def discover_umbrellava_localdns(section):
    for UmbrellaLocalDNSState, UmbrellaLocalDNS1UDPState,UmbrellaLocalDNS1TCPState,UmbrellaLocalDNS2UDPState, UmbrellaLocalDNS2TCPState, UmbrellaLocalDNS3UDPState,UmbrellaLocalDNS3TCPState in section:
      servicename = UmbrellaLocalDNSState[UmbrellaLocalDNSState.find(':')+len(':'):UmbrellaLocalDNSState.rfind(':')]
      yield Service(item=servicename)

register.check_plugin(
    name = "umbrellava_localdns",
    service_name = "UmbrellaVA %s",
    discovery_function = discover_umbrellava_localdns,
    check_function = check_umbrellava_localdns,
)
