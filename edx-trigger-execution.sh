#!/bin/bash

function print_message(){
  echo -e "\n************************************************\n$1\n"
}

function switch-to-project() {
  # Switch to project part
  cd /Users/Users/tester/Downloads/edx-app-test-master/ # replace your project path accordingly
  print_message "switching projects"
  source edx-setup-virtual-env.sh
}


function execute-android-cycle() {
# Android Cycle
pytest -v tests/android/tests/test_android_new_landing.py \
tests/android/tests/test_android_whats_new.py \
tests/android/tests/test_android_register.py \
tests/android/tests/test_android_login.py \
tests/android/tests/test_android_main_dashboard.py \
tests/android/tests/test_android_account.py \
tests/android/tests/test_android_profile.py \
tests/android/tests/test_android_settings.py \
tests/android/tests/test_android_my_courses_list.py \
tests/android/tests/test_android_course_discovery.py \
tests/android/tests/test_android_course_dashboard.py \
tests/android/tests/test_android_course_subsection.py \
--html=report.html --self-contained-html

}

switch-to-project
execute-android-cycle
