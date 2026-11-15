---
id: learning.zephyr-docs.api-file-battery-interrupt-reference.page-5
title: zephyr__drivers__biometrics.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/biometrics_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_drivers\_\_biometrics.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/biometrics_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

生物识别（Biometrics）驱动API的主头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <errno.h>
#include <stddef.h>
#include <zephyr/types.h>
#include <zephyr/syscalls/biometrics.h>
```

查看此文件的源码。

生物识别（Biometrics）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_biometric_5Fcapabilities"></a>

```c
struct biometric_capabilities
```

相关声明：[biometric_capabilities](../driver_model_reference/P027_生物识别能力.md)。

生物识别传感器能力（Biometric Sensor Capabilities）。

<a id="r_biometric_5Fmatch_5Fresult"></a>

```c
struct biometric_match_result
```

相关声明：[biometric_match_result](../driver_model_reference/P030_生物识别匹配结果.md)。

生物特征匹配操作（Biometric Match Operation）的结果。

<a id="r_biometric_5Fcapture_5Fresult"></a>

```c
struct biometric_capture_result
```

相关声明：[biometric_capture_result](../driver_model_reference/P028_生物识别采集结果.md)。

登记采集操作（Enrollment Capture Operation）的结果。

<a id="r_biometric_5Fdriver_5Fapi"></a>

```c
struct biometric_driver_api
```

相关声明：[biometric_driver_api](../driver_model_reference/P029_生物识别驱动接口.md)。

驱动操作（Driver Operations）：生物识别（Biometrics）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_ga09167d8be1ff856b960895b374f9224a"></a>

```c
#define BIOMETRIC_STORAGE_DEVICE BIT(0)
```

相关声明：[BIOMETRIC_STORAGE_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga09167d8be1ff856b960895b374f9224a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

生物识别存储模式（Biometric Storage Modes）。

<a id="r_gaa576d354cd6f8f87fd92bbc02eb3dcb6"></a>

```c
#define BIOMETRIC_STORAGE_HOST BIT(1)
```

相关声明：[BIOMETRIC_STORAGE_HOST](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gaa576d354cd6f8f87fd92bbc02eb3dcb6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

存储在主机系统（Host System）上。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.3\_类型定义（Typedefs）

<a id="r_ga38a8a21a46a8e252792951ce8312294a"></a>

```c
typedef int(* biometric_api_get_capabilities) (const struct device *dev, struct biometric_capabilities *caps)
```

相关声明：[biometric_api_get_capabilities](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#ga38a8a21a46a8e252792951ce8312294a)、[device](../device_reference/P002_设备对象结构.md)、[biometric_capabilities](../driver_model_reference/P027_生物识别能力.md)。

获取传感器能力（Sensor Capabilities）的回调 API。

<a id="r_gad7f71482bb3407bcedf37a7b4b5633be"></a>

```c
typedef int(* biometric_api_attr_set) (const struct device *dev, enum biometric_attribute attr, int32_t val)
```

相关声明：[biometric_api_attr_set](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#gad7f71482bb3407bcedf37a7b4b5633be)、[device](../device_reference/P002_设备对象结构.md)、[biometric_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gafe560b9baea81cbad071ead5015721d0)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置传感器属性（Sensor Attribute）的回调 API。

<a id="r_ga5db0eae1ba88eef3d2fcb99f4a75ff50"></a>

```c
typedef int(* biometric_api_attr_get) (const struct device *dev, enum biometric_attribute attr, int32_t *val)
```

相关声明：[biometric_api_attr_get](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#ga5db0eae1ba88eef3d2fcb99f4a75ff50)、[device](../device_reference/P002_设备对象结构.md)、[biometric_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gafe560b9baea81cbad071ead5015721d0)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

获取传感器属性（Sensor Attribute）的回调 API。

<a id="r_ga2515c347864644dea3906fc3a25c155e"></a>

```c
typedef int(* biometric_api_enroll_start) (const struct device *dev, uint16_t template_id)
```

相关声明：[biometric_api_enroll_start](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#ga2515c347864644dea3906fc3a25c155e)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

开始录入（Enrollment）的回调 API。

<a id="r_ga70253fb65673c4c95c22896ca1bb0641"></a>

```c
typedef int(* biometric_api_enroll_capture) (const struct device *dev, k_timeout_t timeout, struct biometric_capture_result *result)
```

相关声明：[biometric_api_enroll_capture](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#ga70253fb65673c4c95c22896ca1bb0641)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[biometric_capture_result](../driver_model_reference/P028_生物识别采集结果.md)。

采集录入样本（Enrollment Samples）的回调 API。

<a id="r_ga36b3ac91aceeca57ccaaa78619ab603f"></a>

```c
typedef int(* biometric_api_enroll_finalize) (const struct device *dev)
```

相关声明：[biometric_api_enroll_finalize](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#ga36b3ac91aceeca57ccaaa78619ab603f)、[device](../device_reference/P002_设备对象结构.md)。

完成录入（Finalize Enrollment）的回调 API。

<a id="r_gad0aa92ba1e326e98f5963206d548cda3"></a>

```c
typedef int(* biometric_api_enroll_abort) (const struct device *dev)
```

相关声明：[biometric_api_enroll_abort](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#gad0aa92ba1e326e98f5963206d548cda3)、[device](../device_reference/P002_设备对象结构.md)。

中止录入（Abort Enrollment）的回调 API。

<a id="r_gaa86339893ac58e9a1480d013605c2718"></a>

```c
typedef int(* biometric_api_template_store) (const struct device *dev, uint16_t id, const uint8_t *data, size_t size)
```

相关声明：[biometric_api_template_store](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#gaa86339893ac58e9a1480d013605c2718)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

存储模板（Template）的回调 API。

<a id="r_gaf70dbdc914f9a6b89574f1947d821424"></a>

```c
typedef int(* biometric_api_template_read) (const struct device *dev, uint16_t id, uint8_t *data, size_t size)
```

相关声明：[biometric_api_template_read](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#gaf70dbdc914f9a6b89574f1947d821424)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取模板数据（Template Data）的回调 API。

<a id="r_ga182b3b06e09416ba826a46ec346b57d1"></a>

```c
typedef int(* biometric_api_template_delete) (const struct device *dev, uint16_t id)
```

相关声明：[biometric_api_template_delete](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#ga182b3b06e09416ba826a46ec346b57d1)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

删除模板（Template）的回调 API。

<a id="r_ga8196c59e50e8f093383c7a354ceaf694"></a>

```c
typedef int(* biometric_api_template_delete_all) (const struct device *dev)
```

相关声明：[biometric_api_template_delete_all](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#ga8196c59e50e8f093383c7a354ceaf694)、[device](../device_reference/P002_设备对象结构.md)。

删除全部模板（Templates）的回调 API。

<a id="r_gab69ee26aff13e80183e5a929d4f20277"></a>

```c
typedef int(* biometric_api_template_list) (const struct device *dev, uint16_t *ids, size_t max_count, size_t *actual_count)
```

相关声明：[biometric_api_template_list](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#gab69ee26aff13e80183e5a929d4f20277)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

列出模板 ID（Template IDs）的回调 API。

<a id="r_ga5f49256b2d8abf90fdedb33dcd84a95e"></a>

```c
typedef int(* biometric_api_match) (const struct device *dev, enum biometric_match_mode mode, uint16_t template_id, k_timeout_t timeout, struct biometric_match_result *result)
```

相关声明：[biometric_api_match](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#ga5f49256b2d8abf90fdedb33dcd84a95e)、[device](../device_reference/P002_设备对象结构.md)、[biometric_match_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gad84df8a20c10cfacd4b7e547f1b4ca24)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[biometric_match_result](../driver_model_reference/P030_生物识别匹配结果.md)。

开始匹配操作（Matching Operation）的回调 API。

<a id="r_gaa379e427029685e4c73a9dd9ccd3f6c4"></a>

```c
typedef int(* biometric_api_led_control) (const struct device *dev, enum biometric_led_state state)
```

相关声明：[biometric_api_led_control](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#gaa379e427029685e4c73a9dd9ccd3f6c4)、[device](../device_reference/P002_设备对象结构.md)、[biometric_led_state](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga83c3fbd41de6c4f3739880fceadea96f)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

控制发光二极管状态（LED State）的回调 API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.4\_枚举（Enumerations）

<a id="r_ga96ebb7910e37418080a121d043a18bab"></a>

```c
enum biometric_sensor_type { BIOMETRIC_TYPE_FINGERPRINT , BIOMETRIC_TYPE_IRIS , BIOMETRIC_TYPE_FACE , BIOMETRIC_TYPE_VOICE }
```

相关声明：[biometric_sensor_type](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga96ebb7910e37418080a121d043a18bab)、[BIOMETRIC_TYPE_FINGERPRINT](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga96ebb7910e37418080a121d043a18baba946f0e361f258e007fdc003946b21291)、[BIOMETRIC_TYPE_IRIS](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga96ebb7910e37418080a121d043a18baba2b78962d7f87642eccdd98176fa705da)、[BIOMETRIC_TYPE_FACE](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga96ebb7910e37418080a121d043a18baba06b785aa0f5a09c137c9f5b35d28ff59)、[BIOMETRIC_TYPE_VOICE](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga96ebb7910e37418080a121d043a18baba30138a67266a6765908016f70a14336e)。

生物识别传感器类型（Biometrics Sensor Types）。

<a id="r_gad84df8a20c10cfacd4b7e547f1b4ca24"></a>

```c
enum biometric_match_mode { BIOMETRIC_MATCH_VERIFY , BIOMETRIC_MATCH_IDENTIFY }
```

相关声明：[biometric_match_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gad84df8a20c10cfacd4b7e547f1b4ca24)、[BIOMETRIC_MATCH_VERIFY](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggad84df8a20c10cfacd4b7e547f1b4ca24aae262097565b0a8420b1658f362d8e81)、[BIOMETRIC_MATCH_IDENTIFY](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggad84df8a20c10cfacd4b7e547f1b4ca24a677c053cb520e1b07da0cc884c3053ef)。

生物识别匹配模式（Biometric Matching Modes）。

<a id="r_ga83c3fbd41de6c4f3739880fceadea96f"></a>

```c
enum biometric_led_state { BIOMETRIC_LED_OFF , BIOMETRIC_LED_ON , BIOMETRIC_LED_BLINK , BIOMETRIC_LED_BREATHE }
```

相关声明：[biometric_led_state](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga83c3fbd41de6c4f3739880fceadea96f)、[BIOMETRIC_LED_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga83c3fbd41de6c4f3739880fceadea96fab2c1b886bd5c42fa10c488e492bf571a)、[BIOMETRIC_LED_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga83c3fbd41de6c4f3739880fceadea96fa54de3799271229142ffa8e099fbf9ae2)、[BIOMETRIC_LED_BLINK](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga83c3fbd41de6c4f3739880fceadea96faa59be78efbd9b2d4c8a7b8720b04967e)、[BIOMETRIC_LED_BREATHE](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga83c3fbd41de6c4f3739880fceadea96fa49d40e2d9ade1192b968fba235449da7)。

生物识别 LED 状态（Biometric LED States）。

<a id="r_gafe560b9baea81cbad071ead5015721d0"></a>

```c
enum biometric_attribute { BIOMETRIC_ATTR_MATCH_THRESHOLD , BIOMETRIC_ATTR_ENROLLMENT_QUALITY , BIOMETRIC_ATTR_SECURITY_LEVEL , BIOMETRIC_ATTR_TIMEOUT_MS , BIOMETRIC_ATTR_ANTI_SPOOF_LEVEL , BIOMETRIC_ATTR_IMAGE_QUALITY , BIOMETRIC_ATTR_COMMON_COUNT , BIOMETRIC_ATTR_PRIV_START = BIOMETRIC_ATTR_COMMON_COUNT , BIOMETRIC_ATTR_MAX = INT16_MAX }
```

相关声明：[biometric_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gafe560b9baea81cbad071ead5015721d0)、[BIOMETRIC_ATTR_MATCH_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0aa0b5c4fb004ee442265819f1ad1f888f)、[BIOMETRIC_ATTR_ENROLLMENT_QUALITY](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0ac7cc9f7e2420227e96d33b526665cda0)、[BIOMETRIC_ATTR_SECURITY_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0a8af3a6b4fb231c8991543f357a318eec)、[BIOMETRIC_ATTR_TIMEOUT_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0af4ebcb6c0c73f05f6f6279d71d76a3d5)、[BIOMETRIC_ATTR_ANTI_SPOOF_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0aef92b844ead708b1337fa983278e4499)、[BIOMETRIC_ATTR_IMAGE_QUALITY](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0aceaac5e1b094da0b92a927f9d0379071)、[BIOMETRIC_ATTR_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0a29e1b51dfbda37a58642630b44a59ece)、[BIOMETRIC_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0afa83aa1fd1d91ba0753e46d9cf8e098d)、[BIOMETRIC_ATTR_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0a3770042eafa778b907f7598d762f8ca3)。

生物识别属性类型（Biometric Attribute Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.5\_函数（Functions）

<a id="r_gaa335d1d790f5ce609b6de57eaeb1399c"></a>

```c
int biometric_get_capabilities (const struct device *dev, struct biometric_capabilities *caps)
```

相关声明：[biometric_get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gaa335d1d790f5ce609b6de57eaeb1399c)、[device](../device_reference/P002_设备对象结构.md)、[biometric_capabilities](../driver_model_reference/P027_生物识别能力.md)。

获取生物识别传感器的能力（Capabilities）。

<a id="r_ga4ca9b34414ff86b2a5271bbc4c2563df"></a>

```c
int biometric_attr_set (const struct device *dev, enum biometric_attribute attr, int32_t val)
```

相关声明：[biometric_attr_set](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga4ca9b34414ff86b2a5271bbc4c2563df)、[device](../device_reference/P002_设备对象结构.md)、[biometric_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gafe560b9baea81cbad071ead5015721d0)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置生物识别传感器属性（Attribute）。

<a id="r_ga243ad98c425edb68b425be8639b6fcac"></a>

```c
int biometric_attr_get (const struct device *dev, enum biometric_attribute attr, int32_t *val)
```

相关声明：[biometric_attr_get](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga243ad98c425edb68b425be8639b6fcac)、[device](../device_reference/P002_设备对象结构.md)、[biometric_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gafe560b9baea81cbad071ead5015721d0)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

获取生物识别传感器属性（Attribute）。

<a id="r_ga65bdfd912acf5e9503d0f91d5842cf8c"></a>

```c
int biometric_enroll_start (const struct device *dev, uint16_t template_id)
```

相关声明：[biometric_enroll_start](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga65bdfd912acf5e9503d0f91d5842cf8c)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

开始生物特征录入（Biometric Enrollment）。

<a id="r_ga2a5c36eca939da337f38b54b44ef16eb"></a>

```c
int biometric_enroll_capture (const struct device *dev, k_timeout_t timeout, struct biometric_capture_result *result)
```

相关声明：[biometric_enroll_capture](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga2a5c36eca939da337f38b54b44ef16eb)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[biometric_capture_result](../driver_model_reference/P028_生物识别采集结果.md)。

采集录入样本（Enrollment Samples）。

<a id="r_gaf2d6cf698d301c58dbcfb782af96d205"></a>

```c
int biometric_enroll_finalize (const struct device *dev)
```

相关声明：[biometric_enroll_finalize](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gaf2d6cf698d301c58dbcfb782af96d205)、[device](../device_reference/P002_设备对象结构.md)。

完成录入（Enrollment）。

<a id="r_ga330af9905835af25b41e2e9b7fff11e6"></a>

```c
int biometric_enroll_abort (const struct device *dev)
```

相关声明：[biometric_enroll_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga330af9905835af25b41e2e9b7fff11e6)、[device](../device_reference/P002_设备对象结构.md)。

中止录入（Enrollment）。

<a id="r_gae323da0884660fba5b7bcb9b210aec00"></a>

```c
int biometric_template_store (const struct device *dev, uint16_t id, const uint8_t *data, size_t size)
```

相关声明：[biometric_template_store](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gae323da0884660fba5b7bcb9b210aec00)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

存储生物特征模板（Biometric Template）。

<a id="r_ga8be2ec31d1848891327a44cda198b86e"></a>

```c
int biometric_template_read (const struct device *dev, uint16_t id, uint8_t *data, size_t size)
```

相关声明：[biometric_template_read](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga8be2ec31d1848891327a44cda198b86e)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取生物特征模板（Biometric Template）。

<a id="r_ga1fa103e8d4a55ffba82f1b0f65634c16"></a>

```c
int biometric_template_delete (const struct device *dev, uint16_t id)
```

相关声明：[biometric_template_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga1fa103e8d4a55ffba82f1b0f65634c16)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

删除生物特征模板（Biometric Template）。

<a id="r_gab5c9975eff4a737f75710e2f43df39b2"></a>

```c
int biometric_template_delete_all (const struct device *dev)
```

相关声明：[biometric_template_delete_all](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gab5c9975eff4a737f75710e2f43df39b2)、[device](../device_reference/P002_设备对象结构.md)。

删除所有生物特征模板（Biometric Templates）。

<a id="r_ga9de5325164b6ed98427275662a7bb07e"></a>

```c
int biometric_template_list (const struct device *dev, uint16_t *ids, size_t max_count, size_t *actual_count)
```

相关声明：[biometric_template_list](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga9de5325164b6ed98427275662a7bb07e)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

列出已存储的模板 ID（Template IDs）。

<a id="r_ga51d358b76f65d2776dfe4fed79e4afcd"></a>

```c
int biometric_match (const struct device *dev, enum biometric_match_mode mode, uint16_t template_id, k_timeout_t timeout, struct biometric_match_result *result)
```

相关声明：[biometric_match](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga51d358b76f65d2776dfe4fed79e4afcd)、[device](../device_reference/P002_设备对象结构.md)、[biometric_match_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gad84df8a20c10cfacd4b7e547f1b4ca24)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[biometric_match_result](../driver_model_reference/P030_生物识别匹配结果.md)。

执行生物特征匹配（Biometric Matching）。

<a id="r_gaca4596921ea8f1554215d4994da5537e"></a>

```c
int biometric_led_control (const struct device *dev, enum biometric_led_state state)
```

相关声明：[biometric_led_control](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gaca4596921ea8f1554215d4994da5537e)、[device](../device_reference/P002_设备对象结构.md)、[biometric_led_state](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga83c3fbd41de6c4f3739880fceadea96f)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

控制生物识别传感器的 LED。


## 5.6\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P066_biometrics.h_源码浏览.md)
- [biometric_capabilities](../driver_model_reference/P027_生物识别能力.md)
- [biometric_match_result](../driver_model_reference/P030_生物识别匹配结果.md)
- [biometric_capture_result](../driver_model_reference/P028_生物识别采集结果.md)
- [biometric_driver_api](../driver_model_reference/P029_生物识别驱动接口.md)
- [BIOMETRIC_STORAGE_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga09167d8be1ff856b960895b374f9224a)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BIOMETRIC_STORAGE_HOST](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gaa576d354cd6f8f87fd92bbc02eb3dcb6)
- [biometric_api_get_capabilities](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#ga38a8a21a46a8e252792951ce8312294a)
- [device](../device_reference/P002_设备对象结构.md)
- [biometric_api_attr_set](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#gad7f71482bb3407bcedf37a7b4b5633be)
- [biometric_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gafe560b9baea81cbad071ead5015721d0)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [biometric_api_attr_get](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#ga5db0eae1ba88eef3d2fcb99f4a75ff50)
- [biometric_api_enroll_start](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#ga2515c347864644dea3906fc3a25c155e)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [biometric_api_enroll_capture](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#ga70253fb65673c4c95c22896ca1bb0641)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [biometric_api_enroll_finalize](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#ga36b3ac91aceeca57ccaaa78619ab603f)
- [biometric_api_enroll_abort](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#gad0aa92ba1e326e98f5963206d548cda3)
- [biometric_api_template_store](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#gaa86339893ac58e9a1480d013605c2718)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [biometric_api_template_read](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#gaf70dbdc914f9a6b89574f1947d821424)
- [biometric_api_template_delete](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#ga182b3b06e09416ba826a46ec346b57d1)
- [biometric_api_template_delete_all](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#ga8196c59e50e8f093383c7a354ceaf694)
- [biometric_api_template_list](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#gab69ee26aff13e80183e5a929d4f20277)
- [biometric_api_match](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#ga5f49256b2d8abf90fdedb33dcd84a95e)
- [biometric_match_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gad84df8a20c10cfacd4b7e547f1b4ca24)
- [biometric_api_led_control](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md#gaa379e427029685e4c73a9dd9ccd3f6c4)
- [biometric_led_state](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga83c3fbd41de6c4f3739880fceadea96f)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [biometric_sensor_type](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga96ebb7910e37418080a121d043a18bab)
- [BIOMETRIC_TYPE_FINGERPRINT](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga96ebb7910e37418080a121d043a18baba946f0e361f258e007fdc003946b21291)
- [BIOMETRIC_TYPE_IRIS](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga96ebb7910e37418080a121d043a18baba2b78962d7f87642eccdd98176fa705da)
- [BIOMETRIC_TYPE_FACE](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga96ebb7910e37418080a121d043a18baba06b785aa0f5a09c137c9f5b35d28ff59)
- [BIOMETRIC_TYPE_VOICE](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga96ebb7910e37418080a121d043a18baba30138a67266a6765908016f70a14336e)
- [BIOMETRIC_MATCH_VERIFY](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggad84df8a20c10cfacd4b7e547f1b4ca24aae262097565b0a8420b1658f362d8e81)
- [BIOMETRIC_MATCH_IDENTIFY](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggad84df8a20c10cfacd4b7e547f1b4ca24a677c053cb520e1b07da0cc884c3053ef)
- [BIOMETRIC_LED_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga83c3fbd41de6c4f3739880fceadea96fab2c1b886bd5c42fa10c488e492bf571a)
- [BIOMETRIC_LED_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga83c3fbd41de6c4f3739880fceadea96fa54de3799271229142ffa8e099fbf9ae2)
- [BIOMETRIC_LED_BLINK](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga83c3fbd41de6c4f3739880fceadea96faa59be78efbd9b2d4c8a7b8720b04967e)
- [BIOMETRIC_LED_BREATHE](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gga83c3fbd41de6c4f3739880fceadea96fa49d40e2d9ade1192b968fba235449da7)
- [BIOMETRIC_ATTR_MATCH_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0aa0b5c4fb004ee442265819f1ad1f888f)
- [BIOMETRIC_ATTR_ENROLLMENT_QUALITY](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0ac7cc9f7e2420227e96d33b526665cda0)
- [BIOMETRIC_ATTR_SECURITY_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0a8af3a6b4fb231c8991543f357a318eec)
- [BIOMETRIC_ATTR_TIMEOUT_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0af4ebcb6c0c73f05f6f6279d71d76a3d5)
- [BIOMETRIC_ATTR_ANTI_SPOOF_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0aef92b844ead708b1337fa983278e4499)
- [BIOMETRIC_ATTR_IMAGE_QUALITY](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0aceaac5e1b094da0b92a927f9d0379071)
- [BIOMETRIC_ATTR_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0a29e1b51dfbda37a58642630b44a59ece)
- [BIOMETRIC_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0afa83aa1fd1d91ba0753e46d9cf8e098d)
- [BIOMETRIC_ATTR_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ggafe560b9baea81cbad071ead5015721d0a3770042eafa778b907f7598d762f8ca3)
- [biometric_get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gaa335d1d790f5ce609b6de57eaeb1399c)
- [biometric_attr_set](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga4ca9b34414ff86b2a5271bbc4c2563df)
- [biometric_attr_get](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga243ad98c425edb68b425be8639b6fcac)
- [biometric_enroll_start](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga65bdfd912acf5e9503d0f91d5842cf8c)
- [biometric_enroll_capture](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga2a5c36eca939da337f38b54b44ef16eb)
- [biometric_enroll_finalize](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gaf2d6cf698d301c58dbcfb782af96d205)
- [biometric_enroll_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga330af9905835af25b41e2e9b7fff11e6)
- [biometric_template_store](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gae323da0884660fba5b7bcb9b210aec00)
- [biometric_template_read](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga8be2ec31d1848891327a44cda198b86e)
- [biometric_template_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga1fa103e8d4a55ffba82f1b0f65634c16)
- [biometric_template_delete_all](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gab5c9975eff4a737f75710e2f43df39b2)
- [biometric_template_list](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga9de5325164b6ed98427275662a7bb07e)
- [biometric_match](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga51d358b76f65d2776dfe4fed79e4afcd)
- [biometric_led_control](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gaca4596921ea8f1554215d4994da5537e)

<a id="header-details"></a>

---

[上一章](P004_zephyr__bluetooth__services__bas.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__dt-bindings__sensor__adxl355.h_文件参考.md)
