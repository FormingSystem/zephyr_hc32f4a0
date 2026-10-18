---
id: learning.zephyr-docs.api-biometric-mesh-topic-reference.page-1
title: 生物识别（Biometrics）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_生物识别（Biometrics）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

生物识别传感器（Biometric sensors）接口。

<a id="details"></a>

生物识别传感器（Biometric Sensors）接口。自（Since）4.4 起提供，版本（Version）0.1.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 1.1\_主题（Topics）

<a id="r_biometrics_5Finterface_5Fbackend"></a>

相关声明：[生物识别驱动后端 API（Biometrics Driver Backend API）](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md)。

<a id="r_biometrics_5Femulator"></a>

相关声明：[生物识别仿真器测试辅助功能（Emulator test helpers）](../hardware/P495_生物识别仿真测试接口.md)。

生物识别仿真器测试控制函数（Emulator test control functions）。

<a id="header-files"></a>
<a id="files"></a>

## 1.2\_文件（Files）

<a id="r_biometrics_2Eh"></a>

```c
file biometrics.h
```

相关声明：[biometrics.h](../api_file_battery_interrupt_reference/P005_zephyr__drivers__biometrics.h_文件参考.md)。

生物识别（Biometrics）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.3\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.4\_宏定义（Macros）

<a id="r_ga09167d8be1ff856b960895b374f9224a"></a>

```c
#define BIOMETRIC_STORAGE_DEVICE BIT(0)
```

相关声明：[BIOMETRIC_STORAGE_DEVICE](#ga09167d8be1ff856b960895b374f9224a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

生物识别存储模式（Biometric Storage Modes）。

<a id="r_gaa576d354cd6f8f87fd92bbc02eb3dcb6"></a>

```c
#define BIOMETRIC_STORAGE_HOST BIT(1)
```

相关声明：[BIOMETRIC_STORAGE_HOST](#gaa576d354cd6f8f87fd92bbc02eb3dcb6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

存储在主机系统（Host System）上。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.5\_枚举（Enumerations）

<a id="r_ga96ebb7910e37418080a121d043a18bab"></a>

```c
enum biometric_sensor_type { BIOMETRIC_TYPE_FINGERPRINT , BIOMETRIC_TYPE_IRIS , BIOMETRIC_TYPE_FACE , BIOMETRIC_TYPE_VOICE }
```

相关声明：[biometric_sensor_type](#ga96ebb7910e37418080a121d043a18bab)、[BIOMETRIC_TYPE_FINGERPRINT](#gga96ebb7910e37418080a121d043a18baba946f0e361f258e007fdc003946b21291)、[BIOMETRIC_TYPE_IRIS](#gga96ebb7910e37418080a121d043a18baba2b78962d7f87642eccdd98176fa705da)、[BIOMETRIC_TYPE_FACE](#gga96ebb7910e37418080a121d043a18baba06b785aa0f5a09c137c9f5b35d28ff59)、[BIOMETRIC_TYPE_VOICE](#gga96ebb7910e37418080a121d043a18baba30138a67266a6765908016f70a14336e)。

生物识别传感器类型（Biometrics Sensor Types）。

<a id="r_gad84df8a20c10cfacd4b7e547f1b4ca24"></a>

```c
enum biometric_match_mode { BIOMETRIC_MATCH_VERIFY , BIOMETRIC_MATCH_IDENTIFY }
```

相关声明：[biometric_match_mode](#gad84df8a20c10cfacd4b7e547f1b4ca24)、[BIOMETRIC_MATCH_VERIFY](#ggad84df8a20c10cfacd4b7e547f1b4ca24aae262097565b0a8420b1658f362d8e81)、[BIOMETRIC_MATCH_IDENTIFY](#ggad84df8a20c10cfacd4b7e547f1b4ca24a677c053cb520e1b07da0cc884c3053ef)。

生物识别匹配模式（Biometric Matching Modes）。

<a id="r_ga83c3fbd41de6c4f3739880fceadea96f"></a>

```c
enum biometric_led_state { BIOMETRIC_LED_OFF , BIOMETRIC_LED_ON , BIOMETRIC_LED_BLINK , BIOMETRIC_LED_BREATHE }
```

相关声明：[biometric_led_state](#ga83c3fbd41de6c4f3739880fceadea96f)、[BIOMETRIC_LED_OFF](#gga83c3fbd41de6c4f3739880fceadea96fab2c1b886bd5c42fa10c488e492bf571a)、[BIOMETRIC_LED_ON](#gga83c3fbd41de6c4f3739880fceadea96fa54de3799271229142ffa8e099fbf9ae2)、[BIOMETRIC_LED_BLINK](#gga83c3fbd41de6c4f3739880fceadea96faa59be78efbd9b2d4c8a7b8720b04967e)、[BIOMETRIC_LED_BREATHE](#gga83c3fbd41de6c4f3739880fceadea96fa49d40e2d9ade1192b968fba235449da7)。

生物识别 LED 状态（Biometric LED States）。

<a id="r_gafe560b9baea81cbad071ead5015721d0"></a>

```c
enum biometric_attribute { BIOMETRIC_ATTR_MATCH_THRESHOLD , BIOMETRIC_ATTR_ENROLLMENT_QUALITY , BIOMETRIC_ATTR_SECURITY_LEVEL , BIOMETRIC_ATTR_TIMEOUT_MS , BIOMETRIC_ATTR_ANTI_SPOOF_LEVEL , BIOMETRIC_ATTR_IMAGE_QUALITY , BIOMETRIC_ATTR_COMMON_COUNT , BIOMETRIC_ATTR_PRIV_START = BIOMETRIC_ATTR_COMMON_COUNT , BIOMETRIC_ATTR_MAX = INT16_MAX }
```

相关声明：[biometric_attribute](#gafe560b9baea81cbad071ead5015721d0)、[BIOMETRIC_ATTR_MATCH_THRESHOLD](#ggafe560b9baea81cbad071ead5015721d0aa0b5c4fb004ee442265819f1ad1f888f)、[BIOMETRIC_ATTR_ENROLLMENT_QUALITY](#ggafe560b9baea81cbad071ead5015721d0ac7cc9f7e2420227e96d33b526665cda0)、[BIOMETRIC_ATTR_SECURITY_LEVEL](#ggafe560b9baea81cbad071ead5015721d0a8af3a6b4fb231c8991543f357a318eec)、[BIOMETRIC_ATTR_TIMEOUT_MS](#ggafe560b9baea81cbad071ead5015721d0af4ebcb6c0c73f05f6f6279d71d76a3d5)、[BIOMETRIC_ATTR_ANTI_SPOOF_LEVEL](#ggafe560b9baea81cbad071ead5015721d0aef92b844ead708b1337fa983278e4499)、[BIOMETRIC_ATTR_IMAGE_QUALITY](#ggafe560b9baea81cbad071ead5015721d0aceaac5e1b094da0b92a927f9d0379071)、[BIOMETRIC_ATTR_COMMON_COUNT](#ggafe560b9baea81cbad071ead5015721d0a29e1b51dfbda37a58642630b44a59ece)、[BIOMETRIC_ATTR_PRIV_START](#ggafe560b9baea81cbad071ead5015721d0afa83aa1fd1d91ba0753e46d9cf8e098d)、[BIOMETRIC_ATTR_MAX](#ggafe560b9baea81cbad071ead5015721d0a3770042eafa778b907f7598d762f8ca3)。

生物识别属性类型（Biometric Attribute Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.6\_函数（Functions）

<a id="r_gaa335d1d790f5ce609b6de57eaeb1399c"></a>

```c
int biometric_get_capabilities (const struct device *dev, struct biometric_capabilities *caps)
```

相关声明：[biometric_get_capabilities](#gaa335d1d790f5ce609b6de57eaeb1399c)、[device](../device_reference/P002_设备对象结构.md)、[biometric_capabilities](../driver_model_reference/P027_生物识别能力.md)。

获取生物识别传感器的能力（Capabilities）。

<a id="r_ga4ca9b34414ff86b2a5271bbc4c2563df"></a>

```c
int biometric_attr_set (const struct device *dev, enum biometric_attribute attr, int32_t val)
```

相关声明：[biometric_attr_set](#ga4ca9b34414ff86b2a5271bbc4c2563df)、[device](../device_reference/P002_设备对象结构.md)、[biometric_attribute](#gafe560b9baea81cbad071ead5015721d0)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置生物识别传感器属性（Attribute）。

<a id="r_ga243ad98c425edb68b425be8639b6fcac"></a>

```c
int biometric_attr_get (const struct device *dev, enum biometric_attribute attr, int32_t *val)
```

相关声明：[biometric_attr_get](#ga243ad98c425edb68b425be8639b6fcac)、[device](../device_reference/P002_设备对象结构.md)、[biometric_attribute](#gafe560b9baea81cbad071ead5015721d0)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

获取生物识别传感器属性（Attribute）。

<a id="r_ga65bdfd912acf5e9503d0f91d5842cf8c"></a>

```c
int biometric_enroll_start (const struct device *dev, uint16_t template_id)
```

相关声明：[biometric_enroll_start](#ga65bdfd912acf5e9503d0f91d5842cf8c)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

开始生物特征录入（Biometric Enrollment）。

<a id="r_ga2a5c36eca939da337f38b54b44ef16eb"></a>

```c
int biometric_enroll_capture (const struct device *dev, k_timeout_t timeout, struct biometric_capture_result *result)
```

相关声明：[biometric_enroll_capture](#ga2a5c36eca939da337f38b54b44ef16eb)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[biometric_capture_result](../driver_model_reference/P028_生物识别采集结果.md)。

采集录入样本（Enrollment Samples）。

<a id="r_gaf2d6cf698d301c58dbcfb782af96d205"></a>

```c
int biometric_enroll_finalize (const struct device *dev)
```

相关声明：[biometric_enroll_finalize](#gaf2d6cf698d301c58dbcfb782af96d205)、[device](../device_reference/P002_设备对象结构.md)。

完成录入（Enrollment）。

<a id="r_ga330af9905835af25b41e2e9b7fff11e6"></a>

```c
int biometric_enroll_abort (const struct device *dev)
```

相关声明：[biometric_enroll_abort](#ga330af9905835af25b41e2e9b7fff11e6)、[device](../device_reference/P002_设备对象结构.md)。

中止录入（Enrollment）。

<a id="r_gae323da0884660fba5b7bcb9b210aec00"></a>

```c
int biometric_template_store (const struct device *dev, uint16_t id, const uint8_t *data, size_t size)
```

相关声明：[biometric_template_store](#gae323da0884660fba5b7bcb9b210aec00)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

存储生物特征模板（Biometric Template）。

<a id="r_ga8be2ec31d1848891327a44cda198b86e"></a>

```c
int biometric_template_read (const struct device *dev, uint16_t id, uint8_t *data, size_t size)
```

相关声明：[biometric_template_read](#ga8be2ec31d1848891327a44cda198b86e)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取生物特征模板（Biometric Template）。

<a id="r_ga1fa103e8d4a55ffba82f1b0f65634c16"></a>

```c
int biometric_template_delete (const struct device *dev, uint16_t id)
```

相关声明：[biometric_template_delete](#ga1fa103e8d4a55ffba82f1b0f65634c16)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

删除生物特征模板（Biometric Template）。

<a id="r_gab5c9975eff4a737f75710e2f43df39b2"></a>

```c
int biometric_template_delete_all (const struct device *dev)
```

相关声明：[biometric_template_delete_all](#gab5c9975eff4a737f75710e2f43df39b2)、[device](../device_reference/P002_设备对象结构.md)。

删除所有生物特征模板（Biometric Templates）。

<a id="r_ga9de5325164b6ed98427275662a7bb07e"></a>

```c
int biometric_template_list (const struct device *dev, uint16_t *ids, size_t max_count, size_t *actual_count)
```

相关声明：[biometric_template_list](#ga9de5325164b6ed98427275662a7bb07e)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

列出已存储的模板 ID（Template IDs）。

<a id="r_ga51d358b76f65d2776dfe4fed79e4afcd"></a>

```c
int biometric_match (const struct device *dev, enum biometric_match_mode mode, uint16_t template_id, k_timeout_t timeout, struct biometric_match_result *result)
```

相关声明：[biometric_match](#ga51d358b76f65d2776dfe4fed79e4afcd)、[device](../device_reference/P002_设备对象结构.md)、[biometric_match_mode](#gad84df8a20c10cfacd4b7e547f1b4ca24)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[biometric_match_result](../driver_model_reference/P030_生物识别匹配结果.md)。

执行生物特征匹配（Biometric Matching）。

<a id="r_gaca4596921ea8f1554215d4994da5537e"></a>

```c
int biometric_led_control (const struct device *dev, enum biometric_led_state state)
```

相关声明：[biometric_led_control](#gaca4596921ea8f1554215d4994da5537e)、[device](../device_reference/P002_设备对象结构.md)、[biometric_led_state](#ga83c3fbd41de6c4f3739880fceadea96f)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

控制生物识别传感器的 LED。

## 1.7\_详细说明（Detailed Documentation）

<a id="ga09167d8be1ff856b960895b374f9224a"></a>

### `BIOMETRIC_STORAGE_DEVICE`

```c
#define BIOMETRIC_STORAGE_DEVICE BIT(0)
```

```c
#include <zephyr/drivers/biometrics.h>
```

生物识别存储模式（Biometric Storage Modes）。

存储在传感器设备（Sensor Device）上。

<a id="gaa576d354cd6f8f87fd92bbc02eb3dcb6"></a>

### `BIOMETRIC_STORAGE_HOST`

```c
#define BIOMETRIC_STORAGE_HOST BIT(1)
```

```c
#include <zephyr/drivers/biometrics.h>
```

存储在主机系统（Host System）上。

<a id="gafe560b9baea81cbad071ead5015721d0"></a>

### `biometric_attribute`

```c
enum biometric_attribute
```

```c
#include <zephyr/drivers/biometrics.h>
```

生物识别属性类型（Biometric Attribute Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BIOMETRIC_ATTR_MATCH_THRESHOLD` | 接受匹配结果所需的最低置信度分数（Confidence Score），取值范围由传感器决定。 |
| `BIOMETRIC_ATTR_ENROLLMENT_QUALITY` | 接受录入所需的最低质量分数（Quality Score），取值范围由传感器决定。 |
| `BIOMETRIC_ATTR_SECURITY_LEVEL` | 安全级别（Security Level），范围为 1–10；较高值可减少误接受（False Accepts）。 |
| `BIOMETRIC_ATTR_TIMEOUT_MS` | 默认操作超时（Operation Timeout），单位为毫秒。 |
| `BIOMETRIC_ATTR_ANTI_SPOOF_LEVEL` | 防伪检测灵敏度（Anti-Spoofing Detection Sensitivity），范围为 1–10。 |
| `BIOMETRIC_ATTR_IMAGE_QUALITY` | 最近捕获图像的质量分数（Image Quality Score），取值范围由传感器决定；只读。 |
| `BIOMETRIC_ATTR_COMMON_COUNT` | 所有通用生物识别属性（Common Biometric Attributes）的数量。 |
| `BIOMETRIC_ATTR_PRIV_START` | 此值及更高值由具体传感器定义（Sensor Specific）。参见传感器头文件。 |
| `BIOMETRIC_ATTR_MAX` | 描述生物识别属性类型（Biometric Attribute Type）的最大值。 |

<a id="ga83c3fbd41de6c4f3739880fceadea96f"></a>

### `biometric_led_state`

```c
enum biometric_led_state
```

```c
#include <zephyr/drivers/biometrics.h>
```

生物识别 LED 状态（Biometric LED States）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BIOMETRIC_LED_OFF` | LED 关闭（Off）。 |
| `BIOMETRIC_LED_ON` | LED 常亮（On Continuously）。 |
| `BIOMETRIC_LED_BLINK` | LED 闪烁（Blinking）。 |
| `BIOMETRIC_LED_BREATHE` | LED 呼吸效果（Breathing Effect）。 |

<a id="gad84df8a20c10cfacd4b7e547f1b4ca24"></a>

### `biometric_match_mode`

```c
enum biometric_match_mode
```

```c
#include <zephyr/drivers/biometrics.h>
```

生物识别匹配模式（Biometric Matching Modes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BIOMETRIC_MATCH_VERIFY` | 针对指定模板验证（Verify）。 |
| `BIOMETRIC_MATCH_IDENTIFY` | 搜索整个数据库（Search Entire Database）。 |

<a id="ga96ebb7910e37418080a121d043a18bab"></a>

### `biometric_sensor_type`

```c
enum biometric_sensor_type
```

```c
#include <zephyr/drivers/biometrics.h>
```

生物识别传感器类型（Biometrics Sensor Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BIOMETRIC_TYPE_FINGERPRINT` | 指纹传感器（Fingerprint Sensor）。 |
| `BIOMETRIC_TYPE_IRIS` | 虹膜扫描器（Iris Scanner）。 |
| `BIOMETRIC_TYPE_FACE` | 人脸识别（Face Recognition）。 |
| `BIOMETRIC_TYPE_VOICE` | 语音识别（Voice Recognition）。 |

<a id="ga243ad98c425edb68b425be8639b6fcac"></a>

### `biometric_attr_get()`

```c
int biometric_attr_get ( const struct device * dev, enum biometric_attribute attr, int32_t * val )
```

```c
#include <zephyr/drivers/biometrics.h>
```

获取生物识别传感器属性（Attribute）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向生物识别设备（Biometric Device）的指针。 |
| `attr` | 要获取的属性（Attribute）。 |
| `val` | 用于存储属性值的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 设备不支持。 |
| `-EINVAL` | 无效属性（Invalid Attribute）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga4ca9b34414ff86b2a5271bbc4c2563df"></a>

### `biometric_attr_set()`

```c
int biometric_attr_set ( const struct device * dev, enum biometric_attribute attr, int32_t val )
```

```c
#include <zephyr/drivers/biometrics.h>
```

设置生物识别传感器属性（Attribute）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向生物识别设备（Biometric Device）的指针。 |
| `attr` | 要设置的属性（Attribute）。 |
| `val` | 要设置的值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 设备不支持。 |
| `-EINVAL` | 无效的属性或值。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga330af9905835af25b41e2e9b7fff11e6"></a>

### `biometric_enroll_abort()`

```c
int biometric_enroll_abort ( const struct device * dev)
```

```c
#include <zephyr/drivers/biometrics.h>
```

中止录入（Enrollment）。

取消正在进行的录入（Enrollment），并重置录入状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 生物识别设备（Biometric Device）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EALREADY` | 没有录入（Enrollment）正在进行。 |
| `-ENOSYS` | 设备不支持。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga2a5c36eca939da337f38b54b44ef16eb"></a>

### `biometric_enroll_capture()`

```c
int biometric_enroll_capture ( const struct device * dev, k_timeout_t timeout, struct biometric_capture_result * result )
```

```c
#include <zephyr/drivers/biometrics.h>
```

采集录入样本（Enrollment Samples）。

捕获用于录入（Enrollment）的样本。此函数阻塞至捕获到样本或超时到期。在完成录入之前，须多次调用此函数（通常为两次），以收集所有必需样本。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 生物识别设备（Biometric Device）。 |
| `timeout` | 样本捕获超时（Sample Capture Timeout）。 |
| `result` | 指向捕获结果结构体的可选指针，用于获取进度／质量信息；不需要时传入 `NULL`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 尚未开始录入，或已经有足够的样本。 |
| `-ETIMEDOUT` | 等待样本超时。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaf2d6cf698d301c58dbcfb782af96d205"></a>

### `biometric_enroll_finalize()`

```c
int biometric_enroll_finalize ( const struct device * dev)
```

```c
#include <zephyr/drivers/biometrics.h>
```

完成录入（Enrollment）。

完成录入（Enrollment）并存储模板（Template）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 生物识别设备（Biometric Device）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 样本不足。 |
| `-ENOSPC` | 没有空间存储模板（Template）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga65bdfd912acf5e9503d0f91d5842cf8c"></a>

### `biometric_enroll_start()`

```c
int biometric_enroll_start ( const struct device * dev, uint16_t template_id )
```

```c
#include <zephyr/drivers/biometrics.h>
```

开始生物特征录入（Biometric Enrollment）。

开始录入新模板（Template）。调用后，使用 `biometric_enroll_capture()` 捕获样本，再用 `biometric_enroll_finalize()` 完成录入，或用 `biometric_enroll_abort()` 取消。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 生物识别设备（Biometric Device）。 |
| `template_id` | 要分配的模板 ID（Template ID），从 1 开始，有效范围为 1 至 `max_templates`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | `template_id` 无效，或录入已在进行。 |
| `-ENOSPC` | 没有空间存储新模板（Template）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaa335d1d790f5ce609b6de57eaeb1399c"></a>

### `biometric_get_capabilities()`

```c
int biometric_get_capabilities ( const struct device * dev, struct biometric_capabilities * caps )
```

```c
#include <zephyr/drivers/biometrics.h>
```

获取生物识别传感器的能力（Capabilities）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向生物识别设备（Biometric Device）的指针。 |
| `caps` | 指向要填充的能力结构体（Capabilities Structure）的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaca4596921ea8f1554215d4994da5537e"></a>

### `biometric_led_control()`

```c
int biometric_led_control ( const struct device * dev, enum biometric_led_state state )
```

```c
#include <zephyr/drivers/biometrics.h>
```

控制生物识别传感器的 LED。

控制 LED 状态，在操作过程中向用户提供反馈。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 生物识别设备（Biometric Device）。 |
| `state` | 期望的 LED 状态（State）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 设备不支持。 |
| `-EINVAL` | 无效状态（Invalid State）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga51d358b76f65d2776dfe4fed79e4afcd"></a>

### `biometric_match()`

```c
int biometric_match ( const struct device * dev, enum biometric_match_mode mode, uint16_t template_id, k_timeout_t timeout, struct biometric_match_result * result )
```

```c
#include <zephyr/drivers/biometrics.h>
```

执行生物特征匹配（Biometric Matching）。

捕获样本并执行匹配（Matching）。此函数阻塞至匹配完成或超时到期。`BIOMETRIC_MATCH_VERIFY` 模式下针对 `template_id` 验证；`BIOMETRIC_MATCH_IDENTIFY` 模式下搜索所有模板。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 生物识别设备（Biometric Device）。 |
| `mode` | 验证（Verify）或辨识（Identify）模式。 |
| `template_id` | 验证模式的模板 ID；在辨识模式中忽略。 |
| `timeout` | 样本捕获与匹配的超时（Timeout）。 |
| `result` | 指向匹配结果结构体的可选指针，用于获取详细信息；若只需要匹配／不匹配状态，则传入 `NULL`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ETIMEDOUT` | 等待样本超时。 |
| `-ENOENT` | 未找到匹配（No Match Found）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga1fa103e8d4a55ffba82f1b0f65634c16"></a>

### `biometric_template_delete()`

```c
int biometric_template_delete ( const struct device * dev, uint16_t id )
```

```c
#include <zephyr/drivers/biometrics.h>
```

删除生物特征模板（Biometric Template）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向生物识别设备（Biometric Device）的指针。 |
| `id` | 要删除的模板 ID（Template ID）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 无效的 `template_id`。 |
| `-ENOENT` | 未找到模板（Template Not Found）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gab5c9975eff4a737f75710e2f43df39b2"></a>

### `biometric_template_delete_all()`

```c
int biometric_template_delete_all ( const struct device * dev)
```

```c
#include <zephyr/drivers/biometrics.h>
```

删除所有生物特征模板（Biometric Templates）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向生物识别设备（Biometric Device）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 设备不支持。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga9de5325164b6ed98427275662a7bb07e"></a>

### `biometric_template_list()`

```c
int biometric_template_list ( const struct device * dev, uint16_t * ids, size_t max_count, size_t * actual_count )
```

```c
#include <zephyr/drivers/biometrics.h>
```

列出已存储的模板 ID（Template IDs）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向生物识别设备（Biometric Device）的指针。 |
| `ids` | 指向要填入模板 ID（Template IDs）的数组的指针。 |
| `max_count` | 数组可容纳的最大 ID 数量。 |
| `actual_count` | 用于存储实际返回 ID 数量的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 设备不支持。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga8be2ec31d1848891327a44cda198b86e"></a>

### `biometric_template_read()`

```c
int biometric_template_read ( const struct device * dev, uint16_t id, uint8_t * data, size_t size )
```

```c
#include <zephyr/drivers/biometrics.h>
```

读取生物特征模板（Biometric Template）。

获取模板数据（Template Data）。调用者必须分配足够大的数据缓冲区；请在能力信息中查看 `template_size`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向生物识别设备（Biometric Device）的指针。 |
| `id` | 要读取的模板 ID（Template ID）。 |
| `data` | 指向模板数据缓冲区（Template Data Buffer）的指针。 |
| `size` | 数据缓冲区大小。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | `template_id` 无效，或缓冲区过小。 |
| `-ENOENT` | 未找到模板（Template Not Found）。 |
| `-ENOSYS` | 设备不支持。 |

**返回（Returns）**：返回值（Returns）：成功时为写入的字节数，失败时为负 `errno` 值。

<a id="gae323da0884660fba5b7bcb9b210aec00"></a>

### `biometric_template_store()`

```c
int biometric_template_store ( const struct device * dev, uint16_t id, const uint8_t * data, size_t size )
```

```c
#include <zephyr/drivers/biometrics.h>
```

存储生物特征模板（Biometric Template）。

存储预生成的模板（Pre-Generated Template）。用于基于主机的存储系统，或恢复已备份的模板。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向生物识别设备（Biometric Device）的指针。 |
| `id` | 模板 ID（Template ID）。 |
| `data` | 指向模板数据（Template Data）的指针。 |
| `size` | 模板数据大小，单位为字节。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 无效模板数据（Invalid Template Data）。 |
| `-ENOSPC` | 存储已满（Storage Full）。 |
| `-ENOSYS` | 设备不支持。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 1.8\_原页交叉引用（Cross References）

- [生物识别驱动后端 API（Biometrics Driver Backend API）](../api_flash_backend_topic_reference/P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md)
- [生物识别仿真器测试辅助功能（Emulator test helpers）](../hardware/P495_生物识别仿真测试接口.md)
- [biometrics.h](../api_file_battery_interrupt_reference/P005_zephyr__drivers__biometrics.h_文件参考.md)
- [biometric_capabilities](../driver_model_reference/P027_生物识别能力.md)
- [biometric_match_result](../driver_model_reference/P030_生物识别匹配结果.md)
- [biometric_capture_result](../driver_model_reference/P028_生物识别采集结果.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [device](../device_reference/P002_设备对象结构.md)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggafe560b9baea81cbad071ead5015721d0aa0b5c4fb004ee442265819f1ad1f888f"></a>
<a id="ggafe560b9baea81cbad071ead5015721d0ac7cc9f7e2420227e96d33b526665cda0"></a>
<a id="ggafe560b9baea81cbad071ead5015721d0a8af3a6b4fb231c8991543f357a318eec"></a>
<a id="ggafe560b9baea81cbad071ead5015721d0af4ebcb6c0c73f05f6f6279d71d76a3d5"></a>
<a id="ggafe560b9baea81cbad071ead5015721d0aef92b844ead708b1337fa983278e4499"></a>
<a id="ggafe560b9baea81cbad071ead5015721d0aceaac5e1b094da0b92a927f9d0379071"></a>
<a id="ggafe560b9baea81cbad071ead5015721d0a29e1b51dfbda37a58642630b44a59ece"></a>
<a id="ggafe560b9baea81cbad071ead5015721d0afa83aa1fd1d91ba0753e46d9cf8e098d"></a>
<a id="ggafe560b9baea81cbad071ead5015721d0a3770042eafa778b907f7598d762f8ca3"></a>
<a id="gga83c3fbd41de6c4f3739880fceadea96fab2c1b886bd5c42fa10c488e492bf571a"></a>
<a id="gga83c3fbd41de6c4f3739880fceadea96fa54de3799271229142ffa8e099fbf9ae2"></a>
<a id="gga83c3fbd41de6c4f3739880fceadea96faa59be78efbd9b2d4c8a7b8720b04967e"></a>
<a id="gga83c3fbd41de6c4f3739880fceadea96fa49d40e2d9ade1192b968fba235449da7"></a>
<a id="ggad84df8a20c10cfacd4b7e547f1b4ca24aae262097565b0a8420b1658f362d8e81"></a>
<a id="ggad84df8a20c10cfacd4b7e547f1b4ca24a677c053cb520e1b07da0cc884c3053ef"></a>
<a id="gga96ebb7910e37418080a121d043a18baba946f0e361f258e007fdc003946b21291"></a>
<a id="gga96ebb7910e37418080a121d043a18baba2b78962d7f87642eccdd98176fa705da"></a>
<a id="gga96ebb7910e37418080a121d043a18baba06b785aa0f5a09c137c9f5b35d28ff59"></a>
<a id="gga96ebb7910e37418080a121d043a18baba30138a67266a6765908016f70a14336e"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_访问层（Access layer）.md)
