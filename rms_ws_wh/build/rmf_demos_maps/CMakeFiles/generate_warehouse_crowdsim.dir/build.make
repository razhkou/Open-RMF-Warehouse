# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.28

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/daniele/rms_ws_wh/src/rmf_demos_warehouse/rmf_demos_maps

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/daniele/rms_ws_wh/build/rmf_demos_maps

# Utility rule file for generate_warehouse_crowdsim.

# Include any custom commands dependencies for this target.
include CMakeFiles/generate_warehouse_crowdsim.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/generate_warehouse_crowdsim.dir/progress.make

CMakeFiles/generate_warehouse_crowdsim: warehouse_crowdsim

warehouse_crowdsim: maps/warehouse/warehouse.world
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/home/daniele/rms_ws_wh/build/rmf_demos_maps/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating warehouse_crowdsim"
	ros2 run rmf_building_map_tools building_crowdsim /home/daniele/rms_ws_wh/src/rmf_demos_warehouse/rmf_demos_maps/maps/warehouse/warehouse.building.yaml /home/daniele/rms_ws_wh/build/rmf_demos_maps/maps/warehouse/config_resource/ /home/daniele/rms_ws_wh/build/rmf_demos_maps/maps/warehouse/warehouse.world

maps/warehouse/warehouse.world: /home/daniele/rms_ws_wh/src/rmf_demos_warehouse/rmf_demos_maps/maps/warehouse/warehouse.building.yaml
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/home/daniele/rms_ws_wh/build/rmf_demos_maps/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Generating maps/warehouse/warehouse.world"
	ros2 run rmf_building_map_tools building_map_generator gazebo /home/daniele/rms_ws_wh/src/rmf_demos_warehouse/rmf_demos_maps/maps/warehouse/warehouse.building.yaml /home/daniele/rms_ws_wh/build/rmf_demos_maps/maps/warehouse/warehouse.world /home/daniele/rms_ws_wh/build/rmf_demos_maps/maps/warehouse/models
	ros2 run rmf_building_map_tools building_map_model_downloader /home/daniele/rms_ws_wh/src/rmf_demos_warehouse/rmf_demos_maps/maps/warehouse/warehouse.building.yaml -e ~/.gazebo/models

generate_warehouse_crowdsim: CMakeFiles/generate_warehouse_crowdsim
generate_warehouse_crowdsim: maps/warehouse/warehouse.world
generate_warehouse_crowdsim: warehouse_crowdsim
generate_warehouse_crowdsim: CMakeFiles/generate_warehouse_crowdsim.dir/build.make
.PHONY : generate_warehouse_crowdsim

# Rule to build all files generated by this target.
CMakeFiles/generate_warehouse_crowdsim.dir/build: generate_warehouse_crowdsim
.PHONY : CMakeFiles/generate_warehouse_crowdsim.dir/build

CMakeFiles/generate_warehouse_crowdsim.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/generate_warehouse_crowdsim.dir/cmake_clean.cmake
.PHONY : CMakeFiles/generate_warehouse_crowdsim.dir/clean

CMakeFiles/generate_warehouse_crowdsim.dir/depend:
	cd /home/daniele/rms_ws_wh/build/rmf_demos_maps && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/daniele/rms_ws_wh/src/rmf_demos_warehouse/rmf_demos_maps /home/daniele/rms_ws_wh/src/rmf_demos_warehouse/rmf_demos_maps /home/daniele/rms_ws_wh/build/rmf_demos_maps /home/daniele/rms_ws_wh/build/rmf_demos_maps /home/daniele/rms_ws_wh/build/rmf_demos_maps/CMakeFiles/generate_warehouse_crowdsim.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/generate_warehouse_crowdsim.dir/depend

