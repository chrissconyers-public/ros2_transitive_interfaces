
#include "publisher.hpp"

using namespace std::chrono_literals;

namespace sample {

Publisher::Publisher(void)
: Node("publisher") {
  sample_pub_ = create_publisher<interfaces::msg::Sample>("/publisher/sample", 10);
  sample_ext_pub_ = create_publisher<interfaces_ext::msg::SampleExt>("/publisher/sample_ext", 10);
  hb_pub_ = create_publisher<std_msgs::msg::String>("/publisher/hb", 10);
  sample_timer_ = create_wall_timer(200ms, [this](){this->publish_sample();});
  sample_ext_timer_ = create_wall_timer(300ms, [this](){this->publish_sample_ext();});
  hb_timer_ = create_wall_timer(1s, [this](){this->publish_hb();});
}

void Publisher::publish_sample() {
  static int c = 0;
  interfaces::msg::Sample sample;
  sample.field_1 = ++c;
  sample.field_2 = "sample";
  sample_pub_->publish(sample);
}

void Publisher::publish_sample_ext() {
  static int c = 0;
  interfaces_ext::msg::SampleExt sample_ext;
  sample_ext.sample.field_1 = --c;
  sample_ext.sample.field_2 = "sample_ext";
  sample_ext.field_ext_3 = (float)sample_ext.sample.field_1/100.0;
  sample_ext_pub_->publish(sample_ext);
}

void Publisher::publish_hb() {
  std_msgs::msg::String hb;
  hb.data = "beat";
  hb_pub_->publish(hb);
}

}