---
id: learning.zephyr-docs.usb.api-62
title: USB设备固件升级API
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usbd__dfu.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_USB设备固件升级API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usbd__dfu.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 62.1\_阅读说明与来源

译注：本页说明USB大容量存储（MSC）或设备固件升级（DFU）的公开声明。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB设备固件升级（Device Firmware Upgrade，DFU）设备更新API。

USB设备固件升级（Device Firmware Upgrade，DFU）设备更新API。

引入版本（Since）：4.1。

接口版本（Version）：0.1.0。

## 62.2\_宏定义（Macros）

<a id="r_ga24229d3b70d2e61bb1658c35f0be5070"></a>

```c
#define USBD_DFU_DEFINE_IMG(id, iname, ipriv, iread, iwrite, inext)
```

定义USB DFU镜像（Image）。

相关声明：[USBD_DFU_DEFINE_IMG](P062_USB设备固件升级API.md#ga24229d3b70d2e61bb1658c35f0be5070)。

## 62.3\_详细说明（Detailed Documentation）

<a id="ga24229d3b70d2e61bb1658c35f0be5070"></a>

### 62.3.1\_`USBD\_DFU\_DEFINE\_IMG`

```c
#define USBD_DFU_DEFINE_IMG ( id, iname, ipriv, iread, iwrite, inext )
```

```c
#include <zephyr/usb/class/usbd_dfu.h>
```

**宏展开值（Value）**

```c
static __noinit struct usb_if_descriptor usbd_dfu_iface_##id;                   \
                                                                                \
USBD_DESC_STRING_DEFINE(usbd_dfu_str_##id, iname, USBD_DUT_STRING_INTERFACE);   \
                                                                                \
static const STRUCT_SECTION_ITERABLE(usbd_dfu_image, usbd_dfu_image_##id) = {   \
        .name = iname,                                                          \
        .if_desc = &usbd_dfu_iface_##id,                                        \
        .priv = ipriv,                                                          \
        .sd_nd = &usbd_dfu_str_##id,                                            \
        .read_cb = iread,                                                       \
        .write_cb = iwrite,                                                     \
        .next_cb = inext,                                                       \
}
```

定义USB DFU镜像（Image）。

使用此宏创建USB DFU镜像。

回调函数（Callback）必须采用以下形式：

```c
static int read(void *const priv, const uint32_t block, const uint16_t size,
                uint8_t buf[static CONFIG_USBD_DFU_TRANSFER_SIZE])
{
        int len;

        return len;
}

static int write(void *const priv, const uint32_t block, const uint16_t size,
                 const uint8_t buf[static CONFIG_USBD_DFU_TRANSFER_SIZE])
{
        return 0;
}

static bool next(void *const priv,
                 const enum usb_dfu_state state, const enum usb_dfu_state next)
{
        return true;
}
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 链接器据以对已注册镜像排序的标识符 |
| `iname` | 接口描述符（Interface Descriptor）使用的镜像名称 |
| `ipriv` | 传递给回调函数的私有数据指针 |
| `iread` | 镜像读取回调 |
| `iwrite` | 镜像写入回调 |
| `inext` | 通知／确认下一状态 |

> 译注（源码核对）：此宏建立镜像、接口描述符及名称字符串节点，由类初始化枚举；它不写入固件。原文的read回调模板声明int len后直接返回，尚未实现读取，也未初始化len；必须以实际读取字节数或负错误码替换占位实现，不能把这段模板当作可用后端。

## 62.4\_源码跟踪与使用边界

译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_dfu.h)和[官方实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_dfu.c)，摘要见[来源记录](../SOURCES.md)。可沿本仓库的[头文件](../../../include/zephyr/usb/class/usbd_dfu.h)和[类实现](../../../subsys/usb/device_next/class/usbd_dfu.c)跟踪符号；仓库源码可能与网页版本不同。本批没有执行固件构建或硬件操作。

<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructusb__if__descriptor_html"></a>
<a id="astructusbd__dfu__image_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="ausbd__dfu_8h_html_a9096f7fb11c9d84692bc677d8218d01e"></a>

[上一章](P061_USB设备固件升级API说明.md) · [返回大纲](大纲.md) · [下一章](P063_USB固件升级镜像结构.md)
