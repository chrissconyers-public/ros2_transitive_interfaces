
#include "publisher.hpp"

using namespace std::chrono_literals;

namespace sample {

Publisher::Publisher(void)
: Node("publisher") {
  sample_pub_ = create_publisher<interfaces::msg::Sample>("/publisher/sample", 10);
  hb_pub_ = create_publisher<std_msgs::msg::String>("/publisher/hb", 10);
  sample_timer_ = create_wall_timer(200ms, [this](){this->publish_sample();});
  hb_timer_ = create_wall_timer(1s, [this](){this->publish_hb();});
}

void Publisher::publish_sample() {
  static int c = 0;
  interfaces::msg::Sample sample;
  sample.field_1 = ++c;
  sample.field_2 = "sample";
  sample_pub_->publish(sample);
}

void Publisher::publish_hb() {
  std_msgs::msg::String hb;
  hb.data = "beat";
  hb_pub_->publish(hb);
}

}