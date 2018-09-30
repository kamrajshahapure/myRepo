import json
import time
import urllib.request as urllib2
from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY

class JenkinsCollector(object):
  def collect(self):
    metric = GaugeMetricFamily(
        'jenkins_job_last_successful_build_timestamp_seconds',
        'Jenkins build timestamp in unixtime for lastSuccessfulBuild',
        labels=["TestJob"])

    result = json.loads(urllib2.urlopen("https://jsonplaceholder.typicode.com/todos/1").read().decode('UTF-8'))
    print (result)
    metric.add_metric("Aa", result['id'])

    yield metric

if __name__ == "__main__":
  REGISTRY.register(JenkinsCollector())
  start_http_server(1234)
  while True: time.sleep(1)