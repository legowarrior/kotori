from pkgutil import extend_path
from ilaundry.master.server import boot_master
from ilaundry.node.nodeservice import boot_node
from ilaundry.web.server import boot_web
from twisted.internet import reactor
from twisted.python import log

__path__ = extend_path(__path__, __name__)


__doc__ = """iLaundry node service.

Usage:
  ilaundry [--debug]
  ilaundry master [--debug]
  ilaundry node --master=<> [--debug]
  ilaundry (-h | --help)
  ilaundry --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --debug       Enable debug messages

"""
from docopt import docopt


"""
#ilaundry ship <name> move <x> <y> [--speed=<kn>]
#ilaundry ship shoot <x> <y>
#ilaundry mine (set|remove) <x> <y> [--moored | --drifting]
"""

def run():

    arguments = docopt(__doc__, version='iLaundry node service')
    #print arguments
    debug = arguments.get('--debug', False)

    # defaults
    websocket_uri = 'ws://localhost:9000'
    http_port = 35000

    # run node and web gui only, using a remote master
    if arguments['master']:
        boot_master(websocket_uri, debug)

    elif arguments['node']:
        websocket_uri = arguments['--master']
        boot_web(http_port, websocket_uri, debug)
        boot_node(websocket_uri, debug)

    # run master, node and web gui
    else:
        boot_master(websocket_uri, debug)
        boot_web(http_port, websocket_uri, debug)
        boot_node(websocket_uri, debug)

    reactor.run()


if __name__ == '__main__':
    run()
