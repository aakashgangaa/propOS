pushd kubos/apis/app-api/python && pip3 install . --user && popd
pushd kubos/libs/kubos-service && pip3 install . --user && popd
cd kubos
./tools/kubos_verify.sh