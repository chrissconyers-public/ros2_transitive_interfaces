#!/bin/bash

main() {
  conan remove -f "publisher/0.0.1"
  conan create -s compiler.libcxx=libstdc++11 $script_dir/..
}

die() {
  kill -s TERM $TOP_PID
}
set -e
trap "exit 1" TERM
export TOP_PID=$$
script_dir="$(dirname "$(readlink -f "$0")")"
pushd $script_dir > /dev/null
main $@
popd > /dev/null
