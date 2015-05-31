mkdir -p perf_classes
rm -rf perf_classes/*
javac -d perf_classes Performance.java
jar -cvf perf.jar -C perf_classes/ .
