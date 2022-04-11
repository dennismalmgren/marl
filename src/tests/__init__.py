#############################################
# Add the one-folder-up-path
import sys, os
dirn = os.path.dirname(sys.path[0])
sys.path.append(os.path.dirname(sys.path[0]))
#############################################