---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-9
title: zephyr__drivers__haptics.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/haptics_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_drivers\_\_haptics.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/haptics_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

触觉反馈（Haptics）驱动API的主头文件。

<a id="details"></a>

```c
#include <zephyr/audio/codec.h>
#include <zephyr/device.h>
#include <zephyr/drivers/sensor.h>
#include <zephyr/sys/__assert.h>
#include <zephyr/syscalls/haptics.h>
```

查看此文件的源码。

触觉反馈（Haptics）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_haptics_5Fconfig"></a>

```c
union haptics_config
```

相关声明：[haptics_config](../hardware/P151_触觉源配置联合体.md)。

触觉源（Haptics Source）的配置。

<a id="r_haptics_5Fdriver_5Fapi"></a>

```c
struct haptics_driver_api
```

相关声明：[haptics_driver_api](../hardware/P149_触觉驱动操作表.md)。

驱动操作（Driver Operations）：触觉反馈（Haptics）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 9.2\_类型定义（Typedefs）

<a id="r_gae0ec52bbeb07c255044a4257df43a396"></a>

```c
typedef void(* haptics_error_callback_t) (const struct device *dev, const uint32_t errors, void *const user_data)
```

相关声明：[haptics_error_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gae0ec52bbeb07c255044a4257df43a396)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

发生错误时调用的回调函数类型（Callback Function Type）。

<a id="r_ga6d174ac558915159e501abecebc3e327"></a>

```c
typedef int(* haptics_calibrate_t) (const struct device *dev, const uint32_t routine)
```

相关声明：[haptics_calibrate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#ga6d174ac558915159e501abecebc3e327)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为外部执行器（External Actuator）校准触觉反馈驱动（Haptic Driver）。

<a id="r_ga31d60fbee3f7137540ecb7b318d05621"></a>

```c
typedef int(* haptics_monitor_get_t) (const struct device *dev, const enum haptics_monitor monitor, const enum haptics_monitor_type type, struct sensor_value *const val)
```

相关声明：[haptics_monitor_get_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#ga31d60fbee3f7137540ecb7b318d05621)、[device](../device_reference/P002_设备对象结构.md)、[haptics_monitor](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga2a801a325778cfa22765d68bd6f97b2f)、[haptics_monitor_type](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gaf86396239e200ecf8ea00fe339e416ca)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

从触觉反馈驱动（Haptic Driver）获取集成传感器读数（Integrated Sensor Reading）。

<a id="r_ga469bd3e86ed9b71732cd5103988827a2"></a>

```c
typedef int(* haptics_monitor_set_t) (const struct device *dev, const enum haptics_monitor monitor, const bool enable)
```

相关声明：[haptics_monitor_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#ga469bd3e86ed9b71732cd5103988827a2)、[device](../device_reference/P002_设备对象结构.md)、[haptics_monitor](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga2a801a325778cfa22765d68bd6f97b2f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

使能或禁用触觉反馈驱动（Haptic Driver）的集成感测（Integrated Sensing）。

<a id="r_ga10f61b0a2084b083f6ecf5b5901b4e90"></a>

```c
typedef int(* haptics_register_error_callback_t) (const struct device *dev, haptics_error_callback_t cb, void *const user_data)
```

相关声明：[haptics_register_error_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#ga10f61b0a2084b083f6ecf5b5901b4e90)、[device](../device_reference/P002_设备对象结构.md)、[haptics_error_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gae0ec52bbeb07c255044a4257df43a396)。

注册触觉反馈错误（Haptics Errors）的回调函数（Callback）。

<a id="r_ga5b0c848d0677600ab873c37f9e73770e"></a>

```c
typedef int(* haptics_select_source_t) (const struct device *dev, const enum haptics_source src, const union haptics_config *const cfg)
```

相关声明：[haptics_select_source_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#ga5b0c848d0677600ab873c37f9e73770e)、[device](../device_reference/P002_设备对象结构.md)、[haptics_source](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga72bcc5e6627d6079f81ad8488439f7e4)、[haptics_config](../hardware/P151_触觉源配置联合体.md)。

为 `haptics_start_output()` 指定播放源（Playback Source）。

<a id="r_gaedbe20cc622fa0556f7f42ad2013c896"></a>

```c
typedef int(* haptics_set_level_t) (const struct device *dev, const enum haptics_source src, const union haptics_config *const cfg, const uint32_t level)
```

相关声明：[haptics_set_level_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#gaedbe20cc622fa0556f7f42ad2013c896)、[device](../device_reference/P002_设备对象结构.md)、[haptics_source](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga72bcc5e6627d6079f81ad8488439f7e4)、[haptics_config](../hardware/P151_触觉源配置联合体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置触觉效果（Haptic Effects）的强度控制（Level Controls）。

<a id="r_gab5616b157b07df317b3447c9536de1d6"></a>

```c
typedef int(* haptics_set_trigger_t) (const struct device *dev, const uint32_t trigger, const uint32_t types, const enum haptics_source src, const union haptics_config *const cfg, const uint32_t level)
```

相关声明：[haptics_set_trigger_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#gab5616b157b07df317b3447c9536de1d6)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[haptics_source](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga72bcc5e6627d6079f81ad8488439f7e4)、[haptics_config](../hardware/P151_触觉源配置联合体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将触觉效果（Haptic Effect）分配给指定的 GPIO 事件或条件。

<a id="r_gaa6c2ff4b8ed7ae83e4006eb735f61a46"></a>

```c
typedef int(* haptics_start_output_t) (const struct device *dev)
```

相关声明：[haptics_start_output_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#gaa6c2ff4b8ed7ae83e4006eb735f61a46)、[device](../device_reference/P002_设备对象结构.md)。

开始播放触觉效果（Haptic Effect）。

<a id="r_gae34e538c40e259967f5791cc5ebd2707"></a>

```c
typedef int(* haptics_stop_output_t) (const struct device *dev)
```

相关声明：[haptics_stop_output_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#gae34e538c40e259967f5791cc5ebd2707)、[device](../device_reference/P002_设备对象结构.md)。

停止正在进行的触觉效果（Haptic Effect），并在适用时取消所有排队的效果。

<a id="r_gaf595a1038d42d991eaacacfd1946dcf8"></a>

```c
typedef int(* haptics_stream_samples_t) (const struct device *dev, const uint8_t *const samples, const size_t len)
```

相关声明：[haptics_stream_samples_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#gaf595a1038d42d991eaacacfd1946dcf8)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过控制端口（Control Port）以流式方式传输触觉效果所用的 8 位采样。

<a id="r_gab6747d8671126a14fcfd54212ffa54bc"></a>

```c
typedef int(* haptics_trigger_t) (const struct device *dev, const uint32_t trigger, const enum haptics_trigger_type type)
```

相关声明：[haptics_trigger_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#gab6747d8671126a14fcfd54212ffa54bc)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[haptics_trigger_type](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gabd96eff4adc560173e4e887e09dcb34b)。

触发触觉效果（Haptic Effect）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 9.3\_枚举（Enumerations）

<a id="r_gace3de1e9bf3ad759a618405649a5537a"></a>

```c
enum haptics_error_type { HAPTICS_ERROR_OVERCURRENT = BIT(0) , HAPTICS_ERROR_OVERTEMPERATURE = BIT(1) , HAPTICS_ERROR_UNDERVOLTAGE = BIT(2) , HAPTICS_ERROR_OVERVOLTAGE = BIT(3) , HAPTICS_ERROR_DC = BIT(4) }
```

相关声明：[haptics_error_type](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gace3de1e9bf3ad759a618405649a5537a)、[HAPTICS_ERROR_OVERCURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggace3de1e9bf3ad759a618405649a5537aaa7f4e50aaa2dae83fae9a5931fa4be8f)、[HAPTICS_ERROR_OVERTEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggace3de1e9bf3ad759a618405649a5537aaddb6c50258c48229f27cb77a01116087)、[HAPTICS_ERROR_UNDERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggace3de1e9bf3ad759a618405649a5537aac25c879fce04b01e1476e64f4f3cc2cf)、[HAPTICS_ERROR_OVERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggace3de1e9bf3ad759a618405649a5537aa1149ae71af655549c1037cd79d5cee75)、[HAPTICS_ERROR_DC](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggace3de1e9bf3ad759a618405649a5537aa7ad80e7ab92d1deac3df573b1a76b331)。

触觉反馈错误类型（Haptics Error Types）。

<a id="r_ga2a801a325778cfa22765d68bd6f97b2f"></a>

```c
enum haptics_monitor { HAPTICS_MONITOR_BEMF , HAPTICS_MONITOR_CURRENT , HAPTICS_MONITOR_F0 , HAPTICS_MONITOR_RE , HAPTICS_MONITOR_AMBIENT_TEMP , HAPTICS_MONITOR_DIE_TEMP , HAPTICS_MONITOR_VBAT , HAPTICS_MONITOR_VBST , HAPTICS_MONITOR_VOUT , HAPTICS_MONITOR_ALL }
```

相关声明：[haptics_monitor](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga2a801a325778cfa22765d68bd6f97b2f)、[HAPTICS_MONITOR_BEMF](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fa1feeab298cfcabb1d64c87c20042c58f)、[HAPTICS_MONITOR_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fa1f8b833f578dc7dd10edea6e016eb9dd)、[HAPTICS_MONITOR_F0](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2faa7fcff3f46d5e8046bd4282b94808870)、[HAPTICS_MONITOR_RE](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fac7864ee15f177bb81bc38fbdd001b4c0)、[HAPTICS_MONITOR_AMBIENT_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fae9bf20d60ee4f05ec7829ad91d33349a)、[HAPTICS_MONITOR_DIE_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fab5a60de2ff470c8f5f6d4801b8ae10d8)、[HAPTICS_MONITOR_VBAT](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fa566edc86e881aad6de91333d281eefcb)、[HAPTICS_MONITOR_VBST](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fac578fe2b443ef37c969febca703923c0)、[HAPTICS_MONITOR_VOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fa72c99e1f6a03ac2cbb7a9bcfa6a2f0a2)、[HAPTICS_MONITOR_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fae5e1578253a6fa38331bc8b9949c01f8)。

集成感测功能（Integrated Sensing Features）。

<a id="r_gaf86396239e200ecf8ea00fe339e416ca"></a>

```c
enum haptics_monitor_type { HAPTICS_MONITOR_TYPE_MIN , HAPTICS_MONITOR_TYPE_MAX , HAPTICS_MONITOR_TYPE_MEAN , HAPTICS_MONITOR_TYPE_SINGLE }
```

相关声明：[haptics_monitor_type](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gaf86396239e200ecf8ea00fe339e416ca)、[HAPTICS_MONITOR_TYPE_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggaf86396239e200ecf8ea00fe339e416caae3c79a961c91ce44d9238a3a7c8a066a)、[HAPTICS_MONITOR_TYPE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggaf86396239e200ecf8ea00fe339e416caa6fc1b297a872e0c72a8e4e4c21a153b7)、[HAPTICS_MONITOR_TYPE_MEAN](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggaf86396239e200ecf8ea00fe339e416caa5e17304e155cc4478f21a938a90e1955)、[HAPTICS_MONITOR_TYPE_SINGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggaf86396239e200ecf8ea00fe339e416caa9e2eb231c9a49e1a482c921c1943ac1a)。

集成传感器读数的限定符（Qualifiers）。

<a id="r_ga72bcc5e6627d6079f81ad8488439f7e4"></a>

```c
enum haptics_source { HAPTICS_SOURCE_ROM , HAPTICS_SOURCE_RAM , HAPTICS_SOURCE_DAI , HAPTICS_SOURCE_ANALOG , HAPTICS_SOURCE_PWM , HAPTICS_SOURCE_CONTROL_PORT , HAPTICS_SOURCE_ALL }
```

相关声明：[haptics_source](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga72bcc5e6627d6079f81ad8488439f7e4)、[HAPTICS_SOURCE_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4af8ccf96195a0abdd5d162001e57c583c)、[HAPTICS_SOURCE_RAM](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4a3ad50c248973caf8995ba4d405b51e49)、[HAPTICS_SOURCE_DAI](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4afc9e4ce7acf06b4283ccbfe9f72f1083)、[HAPTICS_SOURCE_ANALOG](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4a8fc4dfbe457b0fcda56a9758c1421824)、[HAPTICS_SOURCE_PWM](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4a0b43851947d20791b1103513117d0ac6)、[HAPTICS_SOURCE_CONTROL_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4a7f190ed6633f9fff3c12052037b44075)、[HAPTICS_SOURCE_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4aa8b3a9045924dc3205977bb262151c45)。

触觉反馈播放源（Haptics Playback Sources）。

<a id="r_gabd96eff4adc560173e4e887e09dcb34b"></a>

```c
enum haptics_trigger_type { HAPTICS_TRIGGER_NONE , HAPTICS_TRIGGER_RISING = BIT(0) , HAPTICS_TRIGGER_FALLING = BIT(1) , HAPTICS_TRIGGER_HIGH = BIT(2) , HAPTICS_TRIGGER_LOW = BIT(3) }
```

相关声明：[haptics_trigger_type](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gabd96eff4adc560173e4e887e09dcb34b)、[HAPTICS_TRIGGER_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggabd96eff4adc560173e4e887e09dcb34ba24be8785a5d6b554be611c730465ea52)、[HAPTICS_TRIGGER_RISING](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggabd96eff4adc560173e4e887e09dcb34bae4a997dc3493948814e3dbec94f4dc61)、[HAPTICS_TRIGGER_FALLING](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggabd96eff4adc560173e4e887e09dcb34ba78d963de3dd4a1c03284e02e8aac5e6d)、[HAPTICS_TRIGGER_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggabd96eff4adc560173e4e887e09dcb34ba594bd6df974f1028b103d60d43ad6554)、[HAPTICS_TRIGGER_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggabd96eff4adc560173e4e887e09dcb34ba16d6ece3fd9764d2c79dae48248d53cb)。

GPIO 触发效果选项（GPIO-triggered Effect Options）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.4\_函数（Functions）

<a id="r_gaa8a7f36b4b37f7512f9f46133d9f4d1b"></a>

```c
int haptics_calibrate (const struct device *dev, const uint32_t routine)
```

相关声明：[haptics_calibrate](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gaa8a7f36b4b37f7512f9f46133d9f4d1b)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为外部执行器（External Actuator）校准触觉反馈驱动（Haptic Driver）。

<a id="r_gabf1e580def265fe9bf95f2116d30e6b2"></a>

```c
int haptics_monitor_get (const struct device *dev, const enum haptics_monitor monitor, const enum haptics_monitor_type type, struct sensor_value *const val)
```

相关声明：[haptics_monitor_get](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gabf1e580def265fe9bf95f2116d30e6b2)、[device](../device_reference/P002_设备对象结构.md)、[haptics_monitor](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga2a801a325778cfa22765d68bd6f97b2f)、[haptics_monitor_type](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gaf86396239e200ecf8ea00fe339e416ca)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

从触觉反馈驱动（Haptic Driver）获取集成传感器读数（Integrated Sensor Reading）。

<a id="r_gad379139afa8aff76647f180c80706f79"></a>

```c
int haptics_monitor_set (const struct device *dev, const enum haptics_monitor monitor, const bool enable)
```

相关声明：[haptics_monitor_set](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gad379139afa8aff76647f180c80706f79)、[device](../device_reference/P002_设备对象结构.md)、[haptics_monitor](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga2a801a325778cfa22765d68bd6f97b2f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

使能或禁用触觉反馈驱动（Haptic Driver）的集成感测（Integrated Sensing）。

<a id="r_gaef1b0ecdbeb529f7f10704d259f2f98f"></a>

```c
static int haptics_register_error_callback (const struct device *dev, haptics_error_callback_t cb, void *const user_data)
```

相关声明：[haptics_register_error_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gaef1b0ecdbeb529f7f10704d259f2f98f)、[device](../device_reference/P002_设备对象结构.md)、[haptics_error_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gae0ec52bbeb07c255044a4257df43a396)。

注册触觉反馈错误（Haptics Errors）的回调函数（Callback）。

<a id="r_ga891fa4c05a4844a658603651e8aabfc5"></a>

```c
int haptics_select_source (const struct device *dev, const enum haptics_source src, const union haptics_config *const cfg)
```

相关声明：[haptics_select_source](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga891fa4c05a4844a658603651e8aabfc5)、[device](../device_reference/P002_设备对象结构.md)、[haptics_source](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga72bcc5e6627d6079f81ad8488439f7e4)、[haptics_config](../hardware/P151_触觉源配置联合体.md)。

指定播放源（Playback Source）及相关配置细节。

<a id="r_gaae134ab4f57a7301dbc16cb379f08192"></a>

```c
int haptics_set_level (const struct device *dev, const enum haptics_source src, const union haptics_config *const cfg, const uint32_t level)
```

相关声明：[haptics_set_level](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gaae134ab4f57a7301dbc16cb379f08192)、[device](../device_reference/P002_设备对象结构.md)、[haptics_source](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga72bcc5e6627d6079f81ad8488439f7e4)、[haptics_config](../hardware/P151_触觉源配置联合体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置触觉效果（Haptic Effects）的强度控制（Level Controls）。

<a id="r_ga26851a2c1eafd8da31a3087b0219c6bf"></a>

```c
int haptics_set_trigger (const struct device *dev, const uint32_t trigger, const uint32_t types, const enum haptics_source src, const union haptics_config *const cfg, const uint32_t level)
```

相关声明：[haptics_set_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga26851a2c1eafd8da31a3087b0219c6bf)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[haptics_source](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga72bcc5e6627d6079f81ad8488439f7e4)、[haptics_config](../hardware/P151_触觉源配置联合体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将触觉效果（Haptic Effect）分配给指定的 GPIO 事件或条件。

<a id="r_ga96e0b0fad35d6535adad7536a9411f44"></a>

```c
int haptics_start_output (const struct device *dev)
```

相关声明：[haptics_start_output](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga96e0b0fad35d6535adad7536a9411f44)、[device](../device_reference/P002_设备对象结构.md)。

开始播放触觉效果（Haptic Effect）。

<a id="r_ga42a5fc7e6b6247316cdf356573dbbb33"></a>

```c
int haptics_stop_output (const struct device *dev)
```

相关声明：[haptics_stop_output](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga42a5fc7e6b6247316cdf356573dbbb33)、[device](../device_reference/P002_设备对象结构.md)。

停止正在进行的触觉效果（Haptic Effect），并在适用时取消所有排队的效果。

<a id="r_ga94b7c216edd6adf14a354b64dbc8a396"></a>

```c
int haptics_stream_samples (const struct device *dev, const uint8_t *const samples, const size_t len)
```

相关声明：[haptics_stream_samples](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga94b7c216edd6adf14a354b64dbc8a396)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过控制端口（Control Port）以流式方式传输触觉效果所用的 8 位采样。

<a id="r_gafb18ed221c2ae5e5b643130bc3d3c8ec"></a>

```c
int haptics_trigger (const struct device *dev, const uint32_t trigger, const enum haptics_trigger_type type)
```

相关声明：[haptics_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gafb18ed221c2ae5e5b643130bc3d3c8ec)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[haptics_trigger_type](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gabd96eff4adc560173e4e887e09dcb34b)。

触发触觉效果（Haptic Effect）。


## 9.5\_原页交叉引用（Cross References）

- [zephyr/audio/codec.h](../api_source_supplement_reference/P032_codec.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/sensor.h](../api_source_transport_clock_reference/P024_sensor.h_源码浏览.md)
- [查看此文件的源码。](../api_source_system_reference/P013_haptics.h_源码浏览.md)
- [haptics_config](../hardware/P151_触觉源配置联合体.md)
- [haptics_driver_api](../hardware/P149_触觉驱动操作表.md)
- [haptics_error_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gae0ec52bbeb07c255044a4257df43a396)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [haptics_calibrate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#ga6d174ac558915159e501abecebc3e327)
- [haptics_monitor_get_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#ga31d60fbee3f7137540ecb7b318d05621)
- [haptics_monitor](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga2a801a325778cfa22765d68bd6f97b2f)
- [haptics_monitor_type](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gaf86396239e200ecf8ea00fe339e416ca)
- [sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)
- [haptics_monitor_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#ga469bd3e86ed9b71732cd5103988827a2)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [haptics_register_error_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#ga10f61b0a2084b083f6ecf5b5901b4e90)
- [haptics_select_source_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#ga5b0c848d0677600ab873c37f9e73770e)
- [haptics_source](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga72bcc5e6627d6079f81ad8488439f7e4)
- [haptics_start_output()](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga96e0b0fad35d6535adad7536a9411f44)
- [haptics_set_level_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#gaedbe20cc622fa0556f7f42ad2013c896)
- [haptics_set_trigger_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#gab5616b157b07df317b3447c9536de1d6)
- [haptics_start_output_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#gaa6c2ff4b8ed7ae83e4006eb735f61a46)
- [haptics_stop_output_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#gae34e538c40e259967f5791cc5ebd2707)
- [haptics_stream_samples_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#gaf595a1038d42d991eaacacfd1946dcf8)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [haptics_trigger_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#gab6747d8671126a14fcfd54212ffa54bc)
- [haptics_trigger_type](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gabd96eff4adc560173e4e887e09dcb34b)
- [haptics_error_type](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gace3de1e9bf3ad759a618405649a5537a)
- [HAPTICS_ERROR_OVERCURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggace3de1e9bf3ad759a618405649a5537aaa7f4e50aaa2dae83fae9a5931fa4be8f)
- [HAPTICS_ERROR_OVERTEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggace3de1e9bf3ad759a618405649a5537aaddb6c50258c48229f27cb77a01116087)
- [HAPTICS_ERROR_UNDERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggace3de1e9bf3ad759a618405649a5537aac25c879fce04b01e1476e64f4f3cc2cf)
- [HAPTICS_ERROR_OVERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggace3de1e9bf3ad759a618405649a5537aa1149ae71af655549c1037cd79d5cee75)
- [HAPTICS_ERROR_DC](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggace3de1e9bf3ad759a618405649a5537aa7ad80e7ab92d1deac3df573b1a76b331)
- [HAPTICS_MONITOR_BEMF](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fa1feeab298cfcabb1d64c87c20042c58f)
- [HAPTICS_MONITOR_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fa1f8b833f578dc7dd10edea6e016eb9dd)
- [HAPTICS_MONITOR_F0](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2faa7fcff3f46d5e8046bd4282b94808870)
- [HAPTICS_MONITOR_RE](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fac7864ee15f177bb81bc38fbdd001b4c0)
- [HAPTICS_MONITOR_AMBIENT_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fae9bf20d60ee4f05ec7829ad91d33349a)
- [HAPTICS_MONITOR_DIE_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fab5a60de2ff470c8f5f6d4801b8ae10d8)
- [HAPTICS_MONITOR_VBAT](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fa566edc86e881aad6de91333d281eefcb)
- [HAPTICS_MONITOR_VBST](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fac578fe2b443ef37c969febca703923c0)
- [HAPTICS_MONITOR_VOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fa72c99e1f6a03ac2cbb7a9bcfa6a2f0a2)
- [HAPTICS_MONITOR_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fae5e1578253a6fa38331bc8b9949c01f8)
- [HAPTICS_MONITOR_TYPE_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggaf86396239e200ecf8ea00fe339e416caae3c79a961c91ce44d9238a3a7c8a066a)
- [HAPTICS_MONITOR_TYPE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggaf86396239e200ecf8ea00fe339e416caa6fc1b297a872e0c72a8e4e4c21a153b7)
- [HAPTICS_MONITOR_TYPE_MEAN](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggaf86396239e200ecf8ea00fe339e416caa5e17304e155cc4478f21a938a90e1955)
- [HAPTICS_MONITOR_TYPE_SINGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggaf86396239e200ecf8ea00fe339e416caa9e2eb231c9a49e1a482c921c1943ac1a)
- [HAPTICS_SOURCE_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4af8ccf96195a0abdd5d162001e57c583c)
- [HAPTICS_SOURCE_RAM](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4a3ad50c248973caf8995ba4d405b51e49)
- [HAPTICS_SOURCE_DAI](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4afc9e4ce7acf06b4283ccbfe9f72f1083)
- [HAPTICS_SOURCE_ANALOG](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4a8fc4dfbe457b0fcda56a9758c1421824)
- [HAPTICS_SOURCE_PWM](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4a0b43851947d20791b1103513117d0ac6)
- [HAPTICS_SOURCE_CONTROL_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4a7f190ed6633f9fff3c12052037b44075)
- [HAPTICS_SOURCE_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4aa8b3a9045924dc3205977bb262151c45)
- [HAPTICS_TRIGGER_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggabd96eff4adc560173e4e887e09dcb34ba24be8785a5d6b554be611c730465ea52)
- [HAPTICS_TRIGGER_RISING](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggabd96eff4adc560173e4e887e09dcb34bae4a997dc3493948814e3dbec94f4dc61)
- [HAPTICS_TRIGGER_FALLING](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggabd96eff4adc560173e4e887e09dcb34ba78d963de3dd4a1c03284e02e8aac5e6d)
- [HAPTICS_TRIGGER_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggabd96eff4adc560173e4e887e09dcb34ba594bd6df974f1028b103d60d43ad6554)
- [HAPTICS_TRIGGER_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggabd96eff4adc560173e4e887e09dcb34ba16d6ece3fd9764d2c79dae48248d53cb)
- [haptics_calibrate](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gaa8a7f36b4b37f7512f9f46133d9f4d1b)
- [haptics_monitor_get](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gabf1e580def265fe9bf95f2116d30e6b2)
- [haptics_monitor_set](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gad379139afa8aff76647f180c80706f79)
- [haptics_register_error_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gaef1b0ecdbeb529f7f10704d259f2f98f)
- [haptics_select_source](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga891fa4c05a4844a658603651e8aabfc5)
- [haptics_set_level](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gaae134ab4f57a7301dbc16cb379f08192)
- [haptics_set_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga26851a2c1eafd8da31a3087b0219c6bf)
- [haptics_stop_output](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga42a5fc7e6b6247316cdf356573dbbb33)
- [haptics_stream_samples](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga94b7c216edd6adf14a354b64dbc8a396)
- [haptics_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gafb18ed221c2ae5e5b643130bc3d3c8ec)

<a id="header-details"></a>

---

[上一章](P008_zephyr__drivers__interrupt_controller__gic.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__dt-bindings__sensor__iis2dlpc.h_文件参考.md)
