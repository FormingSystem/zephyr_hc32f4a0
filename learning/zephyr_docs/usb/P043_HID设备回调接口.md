---
id: learning.zephyr-docs.usb.api-43
title: HID设备回调接口
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhid__device__ops.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_HID设备回调接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhid__device__ops.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 43.1\_阅读说明与来源

译注：本页属于[HID通用说明](P040_HID通用说明.md)及其设备接口参考，说明报告描述符、设备回调和报告传输。声明和原注释按官方页面保留，补充解释明确标为源码译注。

[本册大纲](大纲.md)提供本组第40至50章的全部字段参考。

HID 设备用户回调（User Callbacks）。

```c
#include <zephyr/usb/class/usbd_hid.h>
```

HID 设备用户回调（User Callbacks）。

每个设备都依赖用户部分，根据报告描述符定义的功能处理特性报告（Feature Report）、输入报告和输出报告。必须实现哪些回调取决于设备功能。HID 设备的 USB 部分无法解释设备专用报告描述符，只负责 USB 相关部分、传输和请求校验；对它而言，所有报告都是不透明数据。回调从 USB 设备栈线程调用，不得阻塞。

## 43.2\_数据成员（Data Fields）

<a id="r_a8d96a142b963dd257b2dbb64df82181d"></a>

```c
void(* iface_ready )(const struct device *dev, const bool ready)
```

对应接口属于当前活动配置时，接口就绪回调会以 ready 为 true 调用，此时设备例如可以开始提交输入报告。

相关声明：[iface_ready](P043_HID设备回调接口.md#a8d96a142b963dd257b2dbb64df82181d)、[device](../device_reference/P002_设备对象结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

<a id="r_a3632e4f1247bdd3395a3f470b75dca43"></a>

```c
int(* get_report_size )(const struct device *dev, const uint8_t type, const uint8_t id)
```

可选回调，在为处理 HID Get Report 请求分配缓冲区之前调用。

相关声明：[get_report_size](P043_HID设备回调接口.md#a3632e4f1247bdd3395a3f470b75dca43)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_aff034989bee801c143384464eb6a5a9d"></a>

```c
int(* get_report )(const struct device *dev, const uint8_t type, const uint8_t id, const uint16_t len, uint8_t *const buf)
```

处理 HID Get Report 请求时调用此回调，根据 type 参数获取特性、输入或输出报告。

相关声明：[get_report](P043_HID设备回调接口.md#aff034989bee801c143384464eb6a5a9d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

<a id="r_aee855ba756e584cefa09ff4caba09c66"></a>

```c
int(* verify_set_report )(const struct device *dev, const uint8_t type, const uint8_t id, const uint16_t len)
```

处理 HID Set Report 请求时，在收到实际报告载荷之前调用此回调。

相关声明：[verify_set_report](P043_HID设备回调接口.md#aee855ba756e584cefa09ff4caba09c66)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

<a id="r_add555b9782b763d5b411909d07d952b8"></a>

```c
int(* set_report )(const struct device *dev, const uint8_t type, const uint8_t id, const uint16_t len, const uint8_t *const buf)
```

处理 HID Set Report 请求时调用此回调，根据 type 参数设置特性、输入或输出报告。

相关声明：[set_report](P043_HID设备回调接口.md#add555b9782b763d5b411909d07d952b8)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

<a id="r_a48e03408d693d4d9d9dacf6513a36828"></a>

```c
void(* set_idle )(const struct device *dev, const uint8_t id, const uint32_t duration)
```

限制输入报告频率的通知。

相关声明：[set_idle](P043_HID设备回调接口.md#a48e03408d693d4d9d9dacf6513a36828)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_afd8c16e1256945bc15c70439051deb26"></a>

```c
uint32_t(* get_idle )(const struct device *dev, const uint8_t id)
```

如果报告描述符使用报告标识（Report ID），设备必须实现此回调，返回指定报告 ID 对应的持续时间。

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[get_idle](P043_HID设备回调接口.md#afd8c16e1256945bc15c70439051deb26)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ae9290b806b57c9595fad3ec0a65fdca2"></a>

```c
void(* set_protocol )(const struct device *dev, const uint8_t proto)
```

通知主机已从引导协议（Boot Protocol，0）切换到报告协议（Report Protocol，1），或反向切换。

相关声明：[set_protocol](P043_HID设备回调接口.md#ae9290b806b57c9595fad3ec0a65fdca2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ace79e5ef79606daf22b8f39794e9d19e"></a>

```c
void(* input_report_done )(const struct device *dev, const uint8_t *const report)
```

通知通过 hid_device_submit_report() 提交的输入报告已经发送。

相关声明：[input_report_done](P043_HID设备回调接口.md#ace79e5ef79606daf22b8f39794e9d19e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ac58785fc2a44be7c46e0c950fc09f0ac"></a>

```c
void(* output_report )(const struct device *dev, const uint16_t len, const uint8_t *const buf)
```

收到新输出报告时的回调。

相关声明：[output_report](P043_HID设备回调接口.md#ac58785fc2a44be7c46e0c950fc09f0ac)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_a0043b6bf005785274de2b65f341cb588"></a>

```c
void(* sof )(const struct device *dev)
```

可选的帧起始（Start of Frame，SoF）事件回调。

相关声明：[sof](P043_HID设备回调接口.md#a0043b6bf005785274de2b65f341cb588)、[device](../device_reference/P002_设备对象结构.md)。

## 43.3\_详细说明（Detailed Documentation）

<a id="afd8c16e1256945bc15c70439051deb26"></a>

### `get_idle`

```c
uint32_t(* hid_device_ops::get_idle) (const struct device *dev, const uint8_t id)
```

如果报告描述符使用报告标识（Report ID），设备必须实现此回调，返回指定报告 ID 对应的持续时间。

持续时间的分辨率为毫秒。

<a id="aff034989bee801c143384464eb6a5a9d"></a>

### `get_report`

```c
int(* hid_device_ops::get_report) (const struct device *dev, const uint8_t type, const uint8_t id, const uint16_t len, uint8_t *const buf)
```

处理 HID Get Report 请求时调用此回调，根据 type 参数获取特性、输入或输出报告。

如果报告描述符没有报告 ID，id 参数为零。回调实现必须检查参数，例如报告类型是否受支持以及报告长度；返回负值表示不支持的类型或错误，否则返回写入缓冲区的报告长度。

> 译注（源码核对）：当前实现对回调返回值大于0时填充响应长度，返回0或负数则丢弃响应缓冲。不得写出 len 范围；源码中的长度断言发生在回调返回后，不能替代回调自身的边界检查。

<a id="a3632e4f1247bdd3395a3f470b75dca43"></a>

### `get_report_size`

```c
int(* hid_device_ops::get_report_size) (const struct device *dev, const uint8_t type, const uint8_t id)
```

可选回调，在为处理 HID Get Report 请求分配缓冲区之前调用。

回调应校验报告类型、报告 ID 等请求参数，并返回所请求报告的大小。如果报告类型不受支持或报告 ID 未知，应返回零或负值。

实现此回调可将栈的缓冲区分配限制在所请求报告的大小，而不是分配主机提供的 wLength 那么大的缓冲区。未实现时，栈分配大小为 wLength 的缓冲区。

> 译注（源码核对）：当前实现取 MIN(wLength, 回调返回长度) 作为分配大小；返回0或负数时不分配响应缓冲。此回调约束分配容量，随后 get_report 仍需遵守收到的 len 边界。

<a id="a8d96a142b963dd257b2dbb64df82181d"></a>

### `iface_ready`

```c
void(* hid_device_ops::iface_ready) (const struct device *dev, const bool ready)
```

对应接口属于当前活动配置时，接口就绪回调会以 ready 为 true 调用，此时设备例如可以开始提交输入报告。

接口不再活动时，以 ready 为 false 调用该回调。此回调为可选项。

> 译注（源码核对）：ready 对应接口是否处于活动配置，并不等同设备对象已完成系统初始化。没有就绪通知回调时，应用仍需安排正确的报告提交时机。

<a id="ace79e5ef79606daf22b8f39794e9d19e"></a>

### `input_report_done`

```c
void(* hid_device_ops::input_report_done) (const struct device *dev, const uint8_t *const report)
```

通知通过 hid_device_submit_report() 提交的输入报告已经发送。

如果设备不使用此回调，hid_device_submit_report() 将同步处理。

> 译注（源码核对）：当前完成处理在IN分支中没有按 err 区分是否调用此回调，回调原型也不携带错误码。因此这条通知可用于收回缓冲区使用权，不能单独作为主机成功处理报告的证明。同步路径也只是由同一完成处理释放信号量。

<a id="ac58785fc2a44be7c46e0c950fc09f0ac"></a>

### `output_report`

```c
void(* hid_device_ops::output_report) (const struct device *dev, const uint16_t len, const uint8_t *const buf)
```

收到新输出报告时的回调。

仅通过可选的中断 OUT 管道收到报告时，才调用此回调。没有中断 OUT 管道时，通过 set_report() 接收输出报告。如果报告描述符使用报告 ID，主机会先在缓冲区放置 ID，后接报告数据。

> 译注（源码核对）：当前完成处理仅在 err 为0时调用此回调，随后释放请求缓冲区；若应用要异步处理报告，应在回调返回前复制所需数据，不长期保存 buf 指针。

<a id="a48e03408d693d4d9d9dacf6513a36828"></a>

### `set_idle`

```c
void(* hid_device_ops::set_idle) (const struct device *dev, const uint8_t id, const uint32_t duration)
```

限制输入报告频率的通知。

设备应暂停提交输入报告，直到出现新事件或 duration 指定的时间已过。如果报告描述符使用报告 ID，设备必须保存持续时间，并据此处理指定报告。持续时间的分辨率为毫秒。

> 译注（源码核对）：USB Set Idle 请求中的持续时间以4毫秒为单位；当前实现乘以4后交给本回调，所以 duration 已是毫秒，不要再次乘4。

<a id="ae9290b806b57c9595fad3ec0a65fdca2"></a>

### `set_protocol`

```c
void(* hid_device_ops::set_protocol) (const struct device *dev, const uint8_t proto)
```

通知主机已从引导协议（Boot Protocol，0）切换到报告协议（Report Protocol，1），或反向切换。

<a id="add555b9782b763d5b411909d07d952b8"></a>

### `set_report`

```c
int(* hid_device_ops::set_report) (const struct device *dev, const uint8_t type, const uint8_t id, const uint16_t len, const uint8_t *const buf)
```

处理 HID Set Report 请求时调用此回调，根据 type 参数设置特性、输入或输出报告。

如果报告描述符没有报告 ID，id 参数为零。回调实现必须检查参数，例如报告类型是否受支持；返回非零值表示不支持的类型或错误。

<a id="a0043b6bf005785274de2b65f341cb588"></a>

### `sof`

```c
void(* hid_device_ops::sof) (const struct device *dev)
```

可选的帧起始（Start of Frame，SoF）事件回调。

总会存在依赖软件和硬件的抖动（Jitter）及延迟（Latency）。应谨慎使用此回调，不得阻塞，且执行时间应尽可能短。

<a id="aee855ba756e584cefa09ff4caba09c66"></a>

### `verify_set_report`

```c
int(* hid_device_ops::verify_set_report) (const struct device *dev, const uint8_t type, const uint8_t id, const uint16_t len)
```

处理 HID Set Report 请求时，在收到实际报告载荷之前调用此回调。

回调实现应检查参数，例如报告类型是否受支持；返回非零值表示不支持的类型或错误。未实现此回调时，将无条件接收报告载荷。

## 43.4\_源码跟踪与使用边界

通用项目及描述符见[hid.h](../../../include/zephyr/usb/class/hid.h)，新版接口见[usbd_hid.h](../../../include/zephyr/usb/class/usbd_hid.h)和[新版实现](../../../subsys/usb/device_next/class/usbd_hid.c)，旧接口见[usb_hid.h](../../../include/zephyr/usb/class/usb_hid.h)、[旧版实现](../../../subsys/usb/device/class/hid/core.c)及[新版兼容包装](../../../subsys/usb/device_next/class/usbd_hid_api.c)。本仓库版本可能与官方 latest 不同；译注依据保存的[官方通用头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/hid.h)、[新版头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_hid.h)、[新版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_hid.c)、[兼容包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_hid_api.c)和[旧版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/class/hid/core.c)，摘要见[来源记录](../SOURCES.md)。本批未编译、运行或操作USB硬件。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P042_新版HID设备API.md) · [返回大纲](大纲.md) · [下一章](P044_旧版HID类API说明.md)
