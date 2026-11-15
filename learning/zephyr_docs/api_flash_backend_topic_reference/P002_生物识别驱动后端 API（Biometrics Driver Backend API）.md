---
id: learning.zephyr-docs.api-flash-backend-topic-reference.page-2
title: 生物识别驱动后端 API（Biometrics Driver Backend API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_生物识别驱动后端 API（Biometrics Driver Backend API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

此组包含实现生物识别驱动（Biometrics Driver）所需的 API 类型定义、回调签名（Callback Signatures）及其他辅助接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_biometric_5Fdriver_5Fapi"></a>

```c
struct biometric_driver_api
```

相关声明：[biometric_driver_api](../driver_model_reference/P029_生物识别驱动接口.md)。

驱动操作（Driver Operations）：生物识别（Biometrics）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.2\_类型定义（Typedefs）

<a id="r_ga38a8a21a46a8e252792951ce8312294a"></a>

```c
typedef int(* biometric_api_get_capabilities) (const struct device *dev, struct biometric_capabilities *caps)
```

相关声明：[biometric_api_get_capabilities](#ga38a8a21a46a8e252792951ce8312294a)、[device](../device_reference/P002_设备对象结构.md)、[biometric_capabilities](../driver_model_reference/P027_生物识别能力.md)。

获取传感器能力（Sensor Capabilities）的回调 API。

<a id="r_gad7f71482bb3407bcedf37a7b4b5633be"></a>

```c
typedef int(* biometric_api_attr_set) (const struct device *dev, enum biometric_attribute attr, int32_t val)
```

相关声明：[biometric_api_attr_set](#gad7f71482bb3407bcedf37a7b4b5633be)、[device](../device_reference/P002_设备对象结构.md)、[biometric_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gafe560b9baea81cbad071ead5015721d0)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置传感器属性（Sensor Attribute）的回调 API。

<a id="r_ga5db0eae1ba88eef3d2fcb99f4a75ff50"></a>

```c
typedef int(* biometric_api_attr_get) (const struct device *dev, enum biometric_attribute attr, int32_t *val)
```

相关声明：[biometric_api_attr_get](#ga5db0eae1ba88eef3d2fcb99f4a75ff50)、[device](../device_reference/P002_设备对象结构.md)、[biometric_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gafe560b9baea81cbad071ead5015721d0)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

获取传感器属性（Sensor Attribute）的回调 API。

<a id="r_ga2515c347864644dea3906fc3a25c155e"></a>

```c
typedef int(* biometric_api_enroll_start) (const struct device *dev, uint16_t template_id)
```

相关声明：[biometric_api_enroll_start](#ga2515c347864644dea3906fc3a25c155e)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

开始录入（Enrollment）的回调 API。

<a id="r_ga70253fb65673c4c95c22896ca1bb0641"></a>

```c
typedef int(* biometric_api_enroll_capture) (const struct device *dev, k_timeout_t timeout, struct biometric_capture_result *result)
```

相关声明：[biometric_api_enroll_capture](#ga70253fb65673c4c95c22896ca1bb0641)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[biometric_capture_result](../driver_model_reference/P028_生物识别采集结果.md)。

采集录入样本（Enrollment Samples）的回调 API。

<a id="r_ga36b3ac91aceeca57ccaaa78619ab603f"></a>

```c
typedef int(* biometric_api_enroll_finalize) (const struct device *dev)
```

相关声明：[biometric_api_enroll_finalize](#ga36b3ac91aceeca57ccaaa78619ab603f)、[device](../device_reference/P002_设备对象结构.md)。

完成录入（Finalize Enrollment）的回调 API。

<a id="r_gad0aa92ba1e326e98f5963206d548cda3"></a>

```c
typedef int(* biometric_api_enroll_abort) (const struct device *dev)
```

相关声明：[biometric_api_enroll_abort](#gad0aa92ba1e326e98f5963206d548cda3)、[device](../device_reference/P002_设备对象结构.md)。

中止录入（Abort Enrollment）的回调 API。

<a id="r_gaa86339893ac58e9a1480d013605c2718"></a>

```c
typedef int(* biometric_api_template_store) (const struct device *dev, uint16_t id, const uint8_t *data, size_t size)
```

相关声明：[biometric_api_template_store](#gaa86339893ac58e9a1480d013605c2718)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

存储模板（Template）的回调 API。

<a id="r_gaf70dbdc914f9a6b89574f1947d821424"></a>

```c
typedef int(* biometric_api_template_read) (const struct device *dev, uint16_t id, uint8_t *data, size_t size)
```

相关声明：[biometric_api_template_read](#gaf70dbdc914f9a6b89574f1947d821424)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取模板数据（Template Data）的回调 API。

<a id="r_ga182b3b06e09416ba826a46ec346b57d1"></a>

```c
typedef int(* biometric_api_template_delete) (const struct device *dev, uint16_t id)
```

相关声明：[biometric_api_template_delete](#ga182b3b06e09416ba826a46ec346b57d1)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

删除模板（Template）的回调 API。

<a id="r_ga8196c59e50e8f093383c7a354ceaf694"></a>

```c
typedef int(* biometric_api_template_delete_all) (const struct device *dev)
```

相关声明：[biometric_api_template_delete_all](#ga8196c59e50e8f093383c7a354ceaf694)、[device](../device_reference/P002_设备对象结构.md)。

删除全部模板（Templates）的回调 API。

<a id="r_gab69ee26aff13e80183e5a929d4f20277"></a>

```c
typedef int(* biometric_api_template_list) (const struct device *dev, uint16_t *ids, size_t max_count, size_t *actual_count)
```

相关声明：[biometric_api_template_list](#gab69ee26aff13e80183e5a929d4f20277)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

列出模板 ID（Template IDs）的回调 API。

<a id="r_ga5f49256b2d8abf90fdedb33dcd84a95e"></a>

```c
typedef int(* biometric_api_match) (const struct device *dev, enum biometric_match_mode mode, uint16_t template_id, k_timeout_t timeout, struct biometric_match_result *result)
```

相关声明：[biometric_api_match](#ga5f49256b2d8abf90fdedb33dcd84a95e)、[device](../device_reference/P002_设备对象结构.md)、[biometric_match_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gad84df8a20c10cfacd4b7e547f1b4ca24)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[biometric_match_result](../driver_model_reference/P030_生物识别匹配结果.md)。

开始匹配操作（Matching Operation）的回调 API。

<a id="r_gaa379e427029685e4c73a9dd9ccd3f6c4"></a>

```c
typedef int(* biometric_api_led_control) (const struct device *dev, enum biometric_led_state state)
```

相关声明：[biometric_api_led_control](#gaa379e427029685e4c73a9dd9ccd3f6c4)、[device](../device_reference/P002_设备对象结构.md)、[biometric_led_state](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga83c3fbd41de6c4f3739880fceadea96f)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

控制发光二极管状态（LED State）的回调 API。

## 2.3\_详细说明（Detailed Documentation）

<a id="ga5db0eae1ba88eef3d2fcb99f4a75ff50"></a>

### `biometric_api_attr_get`

```c
typedef int(* biometric_api_attr_get) (const struct device *dev, enum biometric_attribute attr, int32_t *val)
```

```c
#include <zephyr/drivers/biometrics.h>
```

获取传感器属性（Sensor Attribute）的回调 API。

参数说明参见 `biometric_attr_get()`。

<a id="gad7f71482bb3407bcedf37a7b4b5633be"></a>

### `biometric_api_attr_set`

```c
typedef int(* biometric_api_attr_set) (const struct device *dev, enum biometric_attribute attr, int32_t val)
```

```c
#include <zephyr/drivers/biometrics.h>
```

设置传感器属性（Sensor Attribute）的回调 API。

参数说明参见 `biometric_attr_set()`。

<a id="gad0aa92ba1e326e98f5963206d548cda3"></a>

### `biometric_api_enroll_abort`

```c
typedef int(* biometric_api_enroll_abort) (const struct device *dev)
```

```c
#include <zephyr/drivers/biometrics.h>
```

中止录入（Abort Enrollment）的回调 API。

参数说明参见 `biometric_enroll_abort()`。

<a id="ga70253fb65673c4c95c22896ca1bb0641"></a>

### `biometric_api_enroll_capture`

```c
typedef int(* biometric_api_enroll_capture) (const struct device *dev, k_timeout_t timeout, struct biometric_capture_result *result)
```

```c
#include <zephyr/drivers/biometrics.h>
```

采集录入样本（Enrollment Samples）的回调 API。

参数说明参见 `biometric_enroll_capture()`。

<a id="ga36b3ac91aceeca57ccaaa78619ab603f"></a>

### `biometric_api_enroll_finalize`

```c
typedef int(* biometric_api_enroll_finalize) (const struct device *dev)
```

```c
#include <zephyr/drivers/biometrics.h>
```

完成录入（Finalize Enrollment）的回调 API。

参数说明参见 `biometric_enroll_finalize()`。

<a id="ga2515c347864644dea3906fc3a25c155e"></a>

### `biometric_api_enroll_start`

```c
typedef int(* biometric_api_enroll_start) (const struct device *dev, uint16_t template_id)
```

```c
#include <zephyr/drivers/biometrics.h>
```

开始录入（Enrollment）的回调 API。

参数说明参见 `biometric_enroll_start()`。

<a id="ga38a8a21a46a8e252792951ce8312294a"></a>

### `biometric_api_get_capabilities`

```c
typedef int(* biometric_api_get_capabilities) (const struct device *dev, struct biometric_capabilities *caps)
```

```c
#include <zephyr/drivers/biometrics.h>
```

获取传感器能力（Sensor Capabilities）的回调 API。

参数说明参见 `biometric_get_capabilities()`。

<a id="gaa379e427029685e4c73a9dd9ccd3f6c4"></a>

### `biometric_api_led_control`

```c
typedef int(* biometric_api_led_control) (const struct device *dev, enum biometric_led_state state)
```

```c
#include <zephyr/drivers/biometrics.h>
```

控制发光二极管状态（LED State）的回调 API。

参数说明参见 `biometric_led_control()`。

<a id="ga5f49256b2d8abf90fdedb33dcd84a95e"></a>

### `biometric_api_match`

```c
typedef int(* biometric_api_match) (const struct device *dev, enum biometric_match_mode mode, uint16_t template_id, k_timeout_t timeout, struct biometric_match_result *result)
```

```c
#include <zephyr/drivers/biometrics.h>
```

开始匹配操作（Matching Operation）的回调 API。

参数说明参见 `biometric_match()`。

<a id="ga182b3b06e09416ba826a46ec346b57d1"></a>

### `biometric_api_template_delete`

```c
typedef int(* biometric_api_template_delete) (const struct device *dev, uint16_t id)
```

```c
#include <zephyr/drivers/biometrics.h>
```

删除模板（Template）的回调 API。

参数说明参见 `biometric_template_delete()`。

<a id="ga8196c59e50e8f093383c7a354ceaf694"></a>

### `biometric_api_template_delete_all`

```c
typedef int(* biometric_api_template_delete_all) (const struct device *dev)
```

```c
#include <zephyr/drivers/biometrics.h>
```

删除全部模板（Templates）的回调 API。

参数说明参见 `biometric_template_delete_all()`。

<a id="gab69ee26aff13e80183e5a929d4f20277"></a>

### `biometric_api_template_list`

```c
typedef int(* biometric_api_template_list) (const struct device *dev, uint16_t *ids, size_t max_count, size_t *actual_count)
```

```c
#include <zephyr/drivers/biometrics.h>
```

列出模板 ID（Template IDs）的回调 API。

参数说明参见 `biometric_template_list()`。

<a id="gaf70dbdc914f9a6b89574f1947d821424"></a>

### `biometric_api_template_read`

```c
typedef int(* biometric_api_template_read) (const struct device *dev, uint16_t id, uint8_t *data, size_t size)
```

```c
#include <zephyr/drivers/biometrics.h>
```

读取模板数据（Template Data）的回调 API。

参数说明参见 `biometric_template_read()`。

<a id="gaa86339893ac58e9a1480d013605c2718"></a>

### `biometric_api_template_store`

```c
typedef int(* biometric_api_template_store) (const struct device *dev, uint16_t id, const uint8_t *data, size_t size)
```

```c
#include <zephyr/drivers/biometrics.h>
```

存储模板（Template）的回调 API。

参数说明参见 `biometric_template_store()`。


## 2.4\_原页交叉引用（Cross References）

- [biometric_driver_api](../driver_model_reference/P029_生物识别驱动接口.md)
- [device](../device_reference/P002_设备对象结构.md)
- [biometric_capabilities](../driver_model_reference/P027_生物识别能力.md)
- [biometric_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gafe560b9baea81cbad071ead5015721d0)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [biometric_capture_result](../driver_model_reference/P028_生物识别采集结果.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [biometric_match_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gad84df8a20c10cfacd4b7e547f1b4ca24)
- [biometric_match_result](../driver_model_reference/P030_生物识别匹配结果.md)
- [biometric_led_state](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga83c3fbd41de6c4f3739880fceadea96f)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [zephyr/drivers/biometrics.h](https://docs.zephyrproject.org/latest/doxygen/html/biometrics_8h.html)
- [biometric_attr_get()](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga243ad98c425edb68b425be8639b6fcac)
- [biometric_attr_set()](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga4ca9b34414ff86b2a5271bbc4c2563df)
- [biometric_enroll_abort()](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga330af9905835af25b41e2e9b7fff11e6)
- [biometric_enroll_capture()](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga2a5c36eca939da337f38b54b44ef16eb)
- [biometric_enroll_finalize()](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gaf2d6cf698d301c58dbcfb782af96d205)
- [biometric_enroll_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga65bdfd912acf5e9503d0f91d5842cf8c)
- [biometric_get_capabilities()](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gaa335d1d790f5ce609b6de57eaeb1399c)
- [biometric_led_control()](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gaca4596921ea8f1554215d4994da5537e)
- [biometric_match()](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga51d358b76f65d2776dfe4fed79e4afcd)
- [biometric_template_delete()](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga1fa103e8d4a55ffba82f1b0f65634c16)
- [biometric_template_delete_all()](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gab5c9975eff4a737f75710e2f43df39b2)
- [biometric_template_list()](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga9de5325164b6ed98427275662a7bb07e)
- [biometric_template_read()](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga8be2ec31d1848891327a44cda198b86e)
- [biometric_template_store()](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#gae323da0884660fba5b7bcb9b210aec00)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P001_ADXL355 API主题.md) · [返回大纲](大纲.md) · [下一章](P003_微芯（Microchip）.md)
