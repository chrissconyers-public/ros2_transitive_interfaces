
#pragma once

#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp> 
#include <interfaces/msg/sample.hpp>
#include <interfaces_ext/msg/sample_ext.hpp>

namespace sample {

class Publisher : public rclcpp::Node {
public:
  rclcpp::Publisher<interfaces::msg::Sample>::SharedPtr sample_pub_ = nullptr;
  rclcpp::Publisher<interfaces_ext::msg::SampleExt>::SharedPtr sample_ext_pub_ = nullptr;
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr hb_pub_ = nullptr;
  rclcpp::TimerBase::SharedPtr sample_timer_ = nullptr;
  rclcpp::TimerBase::SharedPtr sample_ext_timer_ = nullptr;
  rclcpp::TimerBase::SharedPtr hb_timer_ = nullptr;

  Publisher(void);
  void publish_sample();
  void publish_sample_ext();
  void publish_hb();
};

}