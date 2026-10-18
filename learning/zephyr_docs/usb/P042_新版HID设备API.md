---
id: learning.zephyr-docs.usb.api-42
title: 新版HID设备API
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usbd__hid__device.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_新版HID设备API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usbd__hid__device.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 42.1\_阅读说明与来源

译注：本页属于[HID通用说明](P040_HID通用说明.md)及其设备接口参考，说明报告描述符、设备回调和报告传输。声明和原注释按官方页面保留，补充解释明确标为源码译注。

[本册大纲](大纲.md)提供本组第40至50章的全部字段参考。

USBD HID 设备 API。

USBD HID 设备 API。

引入版本（Since）：3.7。

接口版本（Version）：0.4.0。

## 42.2\_数据结构（Data Structures）

<a id="r_hid_5Fdevice_5Fops"></a>

```c
struct hid_device_ops
```

HID 设备用户回调（User Callbacks）。

相关声明：[hid_device_ops](P043_HID设备回调接口.md)。

## 42.3\_枚举（Enumerations）

<a id="r_gabfdd923d3dea1fc17d6c21f4ad7dab1d"></a>

```c
enum {
    HID_REPORT_TYPE_INPUT = 1,
    HID_REPORT_TYPE_OUTPUT,
    HID_REPORT_TYPE_FEATURE
}
```

HID 报告类型（Report Types），用于 Get Report／Set Report 请求。

相关声明：[HID_REPORT_TYPE_INPUT](P042_新版HID设备API.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1da451c0c5bb29aa79f5ce554ac9a914acd)、[HID_REPORT_TYPE_OUTPUT](P042_新版HID设备API.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1dac019f1ccb72d64b8ce9dc5c5d952f8a3)、[HID_REPORT_TYPE_FEATURE](P042_新版HID设备API.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1dadb047f4ed99575941ca9d857244f5aea)。

## 42.4\_函数（Functions）

<a id="r_gabb4502a7c3ab5d2400c039549577f4d0"></a>

```c
int hid_device_register (const struct device *dev, const uint8_t *const rdesc, const uint16_t rsize, const struct hid_device_ops *const ops)
```

注册 HID 设备报告描述符（Report Descriptor）和用户回调。

相关声明：[hid_device_register](P042_新版HID设备API.md#gabb4502a7c3ab5d2400c039549577f4d0)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[hid_device_ops](P043_HID设备回调接口.md)。

<a id="r_ga547f99b1089a4d65a297faa5d6e8edd8"></a>

```c
int hid_device_submit_report (const struct device *dev, const uint16_t size, const uint8_t *const report)
```

提交新的输入报告（Input Report）。

相关声明：[hid_device_submit_report](P042_新版HID设备API.md#ga547f99b1089a4d65a297faa5d6e8edd8)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_gaa5d319acba8a671537f1ee6a2ea7559e"></a>

```c
int hid_device_set_in_polling (const struct device *dev, const unsigned int period_us)
```

设置输入报告的轮询周期（Polling Period）。

相关声明：[hid_device_set_in_polling](P042_新版HID设备API.md#gaa5d319acba8a671537f1ee6a2ea7559e)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)。

<a id="r_gac5b27822922030734341db4b41435cb6"></a>

```c
int hid_device_set_out_polling (const struct device *dev, const unsigned int period_us)
```

设置输出报告（Output Report）的轮询周期。

相关声明：[hid_device_set_out_polling](P042_新版HID设备API.md#gac5b27822922030734341db4b41435cb6)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)。

## 42.5\_详细说明（Detailed Documentation）

<a id="gabfdd923d3dea1fc17d6c21f4ad7dab1d"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/usb/class/usbd_hid.h>
```

HID 报告类型（Report Types），用于 Get Report／Set Report 请求。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HID_REPORT_TYPE_INPUT` |  |
| `HID_REPORT_TYPE_OUTPUT` |  |
| `HID_REPORT_TYPE_FEATURE` |  |

<a id="gabb4502a7c3ab5d2400c039549577f4d0"></a>

### `hid_device_register()`

```c
int hid_device_register ( const struct device * dev, const uint8_t *const rdesc, const uint16_t rsize, const struct hid_device_ops *const ops )
```

```c
#include <zephyr/usb/class/usbd_hid.h>
```

注册 HID 设备报告描述符（Report Descriptor）和用户回调。

设备必须在 USB 设备支持初始化和启用之前注册报告描述符和用户回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向 HID 设备的指针。 |
| `[in] rdesc` | 指向 HID 报告描述符的指针。 |
| `[in] rsize` | HID 报告描述符的大小。 |
| `[in] ops` | 指向 HID 设备回调的指针。 |

> 译注（源码核对）：当前实现保存报告描述符和回调表指针，不复制它们，须保证使用期间有效。类已初始化返回 -EALREADY；ops 或 get_report 缺失返回 -EINVAL。当前还对声明了OUT端点的设备检查 set_report，对支持引导接口的设备检查 set_protocol。

<a id="gaa5d319acba8a671537f1ee6a2ea7559e"></a>

### `hid_device_set_in_polling()`

```c
int hid_device_set_in_polling ( const struct device * dev, const unsigned int period_us )
```

```c
#include <zephyr/usb/class/usbd_hid.h>
```

设置输入报告的轮询周期（Polling Period）。

类似于设备树属性 in-polling-period-us，但允许在运行时设置不同的轮询周期。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向 HID 设备的指针。 |
| `[in] period_us` | 轮询周期，单位为微秒。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | API 未启用时返回。 |

**注意（Attention）**：仅在启用 Kconfig 选项 CONFIG_USBD_HID_SET_POLLING_PERIOD 时可用。

**返回（Returns）**：成功时为 0，失败时为负 errno 错误码。

> 译注（源码核对）：“运行时”并不表示已枚举后可随时修改。当前实现检查 HID_DEV_CLASS_INITIALIZED，类已初始化返回 -EBUSY；周期按全速／高速的端点间隔编码写入描述符，输入单位仍为微秒。

<a id="gac5b27822922030734341db4b41435cb6"></a>

### `hid_device_set_out_polling()`

```c
int hid_device_set_out_polling ( const struct device * dev, const unsigned int period_us )
```

```c
#include <zephyr/usb/class/usbd_hid.h>
```

设置输出报告（Output Report）的轮询周期。

类似于设备树属性 out-polling-period-us，但允许在运行时设置不同的轮询周期。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向 HID 设备的指针。 |
| `[in] period_us` | 轮询周期，单位为微秒。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | API 未启用时返回。 |

**注意（Attention）**：仅在启用 Kconfig 选项 CONFIG_USBD_HID_SET_POLLING_PERIOD 时可用。

**返回（Returns）**：成功时为 0，失败时为负 errno 错误码。

> 译注（源码核对）：当前实现同样要求类尚未初始化，否则返回 -EBUSY；没有输出端点时返回 -ENOTSUP。它设置中断OUT端点描述符的轮询间隔，不改变控制传输 Set Report 的请求频率。

<a id="ga547f99b1089a4d65a297faa5d6e8edd8"></a>

### `hid_device_submit_report()`

```c
int hid_device_submit_report ( const struct device * dev, const uint16_t size, const uint8_t *const report )
```

```c
#include <zephyr/usb/class/usbd_hid.h>
```

提交新的输入报告（Input Report）。

提交一个新的输入报告，通过中断 IN 管道（Interrupt IN Pipe）发送。原文说明：如果 sync 为 true，函数会阻塞直到报告发送完成。如果设备未提供 input_report_done() 回调，hid_device_submit_report() 将同步处理。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向 HID 设备的指针。 |
| `[in] size` | 输入报告大小。 |
| `[in] report` | 输入报告缓冲区，必须满足对齐要求。 |

**返回（Returns）**：成功时为 0，失败时为负 errno 错误码。

> 译注（源码核对）：当前原型只有 dev、size、report 三个参数，没有 sync 参数；原文关于 sync 的句子是遗留说明。当前实现以 input_report_done 是否存在决定行为：没有回调则等待信号量，有回调则入队后返回。实现用外部缓冲区承载报告，不复制载荷；异步发送完成前不得改写或释放 report。类未启用返回 -EACCES，分配失败返回 -ENOMEM。实现先检查 sizeof(void *) 对齐，内部外部缓冲分配还检查 IS_UDC_ALIGNED；应按[USB缓冲区宏](P039_USB缓冲区宏与定义.md)准备存储，不能只依赖普通字节数组的默认对齐。

## 42.6\_源码跟踪与使用边界

通用项目及描述符见[hid.h](../../../include/zephyr/usb/class/hid.h)，新版接口见[usbd_hid.h](../../../include/zephyr/usb/class/usbd_hid.h)和[新版实现](../../../subsys/usb/device_next/class/usbd_hid.c)，旧接口见[usb_hid.h](../../../include/zephyr/usb/class/usb_hid.h)、[旧版实现](../../../subsys/usb/device/class/hid/core.c)及[新版兼容包装](../../../subsys/usb/device_next/class/usbd_hid_api.c)。本仓库版本可能与官方 latest 不同；译注依据保存的[官方通用头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/hid.h)、[新版头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_hid.h)、[新版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_hid.c)、[兼容包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_hid_api.c)和[旧版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/class/hid/core.c)，摘要见[来源记录](../SOURCES.md)。本批未编译、运行或操作USB硬件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggabfdd923d3dea1fc17d6c21f4ad7dab1da451c0c5bb29aa79f5ce554ac9a914acd"></a>
<a id="ggabfdd923d3dea1fc17d6c21f4ad7dab1dac019f1ccb72d64b8ce9dc5c5d952f8a3"></a>
<a id="ggabfdd923d3dea1fc17d6c21f4ad7dab1dadb047f4ed99575941ca9d857244f5aea"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P041_新版HID设备API说明.md) · [返回大纲](大纲.md) · [下一章](P043_HID设备回调接口.md)
