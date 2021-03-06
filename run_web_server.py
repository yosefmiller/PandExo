# To launch the GUI:
# On ubuntu/linux, run:
# > cd /path/to/this/directory/
# > sudo screen -S "Pandexo Server"
# > sudo python3 run_web_server.py
# This will enable the web server to run as a background process.
#
# The same applies for running a Jupyter IPython Notebook:
# > cd /path/to/this/directory/
# > sudo screen -S "Jupyter IPython Notebook"
# > sudo jupyter notebook --allow-root
#
# To leave the screen:
# Press [Ctrl-A] then [Ctrl-D]
#
# To reconnect to screen:
# > screen -ls
# > screen -r [PID of Pandexo Server]
#
# If the GUI is interrupted due to a server error, kill the process first:
# > ps -a
# > sudo kill [PID of sudo and python]
# A quick one liner to kill all PIDs returned from `ps -a`:
# > sudo kill `ps -a | awk 'NR>1 {print $1}' | tr '\n' ' ' | awk '{print "\n"$0"\n"}'`
# Then reconnect to screen (see above)
# Then relaunch the GUI (see above)

import pandexo.engine.run_online as ro
ro.main()