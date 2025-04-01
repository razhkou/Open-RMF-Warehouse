# Open-RMF-Warehouse
Это репозиторий с моделью роботизированного склада на платформе Open-RMF. Требования для запуска модели: Ubuntu 24.04 LTS, ROS 2 Jazzy, Gazebo Harmonic. Для запуска модели также требуется установить Open-RMF. Инструкции по установке: https://github.com/open-rmf/rmf
Для запуска модели выполните в терминале source /opt/ros/jazzy/setup.bash && source /install/setup.bash, а затем выпонить ros2 launch rmf_demos_gz warehouse.launch.xml
Для отправки задач роботам во втором терминале выполнить source /opt/ros/jazzy/setup.bash && source /install/setup.bash, а затем выполнить python3 send_delivery.py
