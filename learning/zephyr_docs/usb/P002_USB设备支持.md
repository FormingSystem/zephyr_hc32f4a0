---
id: learning.zephyr-docs.usb.usb-device
title: USB设备支持
kind: reference
status: maintained
domains: [zephyr, usb]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/usb/device_next/usb_device.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第2章\_USB设备支持

原文：[USB device support](https://docs.zephyrproject.org/latest/services/connectivity/usb/device_next/usb_device.html)。读取日期：2026-10-12，`latest`。

## 2.1\_概述

**通用串行总线（Universal Serial Bus，USB）** 设备支持由 **USB设备控制器（USB Device Controller，UDC）**驱动、[UDC 驱动 API](P029_USB设备控制器API说明.md#udc-api)、USB 设备栈和 [USB 设备栈 API](P014_USB设备栈API说明.md#usbd-api)组成。UDC 驱动 **应用程序编程接口（Application Programming Interface，API）** 为 USB 设备控制器提供通用、与厂商无关的接口。虽然这些层次之间有清晰的划分，但 UDC 驱动 API 专门用于服务 Zephyr 的 USB 设备栈。

设备栈支持多个设备控制器：**片上系统（System on Chip，SoC）** 如果包含多个控制器，可以同时使用它们。设备栈支持全速和高速设备控制器，也支持在运行时向一个配置注册多个功能或类实例，以及稍后更改配置。它内置多种 USB 类，并提供实现自定义 USB 功能的 API。

> 译注：“运行时配置”不表示能在已初始化状态下任意修改描述符。具体修改边界见 2.3.6：先关闭设备栈，再重新配置和初始化。

## 2.2\_示例

- [USB HID 键盘](P051_HID键盘示例.md#usb-hid-keyboard)。
- [USB Audio 异步显式反馈](P091_USB音频显式反馈示例.md#uac2-explicit-feedback)。
- [USB Audio 异步隐式反馈](P092_USB音频隐式反馈示例.md#uac2-implicit-feedback)。
- [USB Video 摄像头](P124_USB视频摄像头示例.md#uvc)。
- [HCI USB](P190_蓝牙HCIUSB控制器示例.md#bluetooth_hci_usb)。
- [USB CDC ACM UART](P054_CDCACM串口示例.md#usb-cdc-acm)。
- [通过 USB CDC ACM 使用控制台](P055_CDCACM控制台示例.md#usb-cdc-acm-console)。
- [USB 大容量存储](P060_USB大容量存储示例.md#usb-mass)。
- [USB HID 鼠标](P052_HID鼠标示例.md#usb-hid-mouse)。
- [zperf 网络流量发生器](https://docs.zephyrproject.org/latest/samples/net/zperf/README.html#zperf)。要为 USB 设备支持构建该示例，需直接或通过 west 指定配置覆盖文件 `-DEXTRA_CONF_FILE=overlay-usbd.conf` 和设备树覆盖文件 `-DDTC_OVERLAY_FILE=usbd_cdc_ecm.overlay`。

## 2.3\_配置并启用USB设备支持

Zephyr 项目仓库中的 USB 设备示例使用公共文件 [samples/subsys/usb/common/sample_usbd_init.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/usb/common/sample_usbd_init.c)完成实例化、配置和初始化。以下代码片段取自该文件。示例中以 `SAMPLE_USBD_` 为前缀的 USB Samples Kconfig 选项，其默认值专用于 Zephyr 项目，适用范围仅限项目示例。使用下面的代码时，必须将这些 Kconfig 选项及其他默认值替换为适合自身应用或硬件的值。

### 2.3.1\_定义设备上下文

USB 设备栈需要一个**上下文（Context）**结构来管理属性和运行时数据。建议使用 `USBD_DEVICE_DEFINE` 宏定义设备上下文，它会创建一个具有指定名称的静态 `usbd_context` 变量。可以实例化任意数量的上下文。一个 USB 控制器设备可以分配给多个上下文，但同一时刻只能初始化并使用其中一个。应用不得直接读取或修改上下文属性。

```c
/*
 * Instantiate a context named sample_usbd using the default USB device
 * controller, the Zephyr project vendor ID, and the sample product ID.
 * Zephyr project vendor ID must not be used outside of Zephyr samples.
 */
USBD_DEVICE_DEFINE(sample_usbd,
		   DEVICE_DT_GET(DT_NODELABEL(zephyr_udc0)),
		   CONFIG_SAMPLE_USBD_VID, CONFIG_SAMPLE_USBD_PID);
```

> 译注：示例中的 `zephyr_udc0` 是默认 USB 设备控制器节点标签；本例不构成本仓库 HC32 控制器、时钟、端点或引脚配置已经可用的证明。Zephyr 的厂商 ID 不能用于 Zephyr 示例之外的产品，见[厂商与产品标识](P004_USB厂商与产品标识.md)。

### 2.3.2\_创建并添加字符串描述符

USB 设备可以提供制造商、产品和序列号**字符串描述符（String Descriptor）**。应用应分别使用 `USBD_DESC_MANUFACTURER_DEFINE`、`USBD_DESC_PRODUCT_DEFINE` 和 `USBD_DESC_SERIAL_NUMBER_DEFINE` 宏实例化它们。使用字符串描述符还需要通过 `USBD_DESC_LANG_DEFINE` 宏创建一个**语言描述符（Language Descriptor）**实例。

> 译注：描述符（Descriptor）是设备向主机提供的结构化说明；这里的字符串描述符提供可读名称，语言描述符说明这些字符串支持的语言。

```c
USBD_DESC_LANG_DEFINE(sample_lang);
USBD_DESC_MANUFACTURER_DEFINE(sample_mfr, CONFIG_SAMPLE_USBD_MANUFACTURER);
USBD_DESC_PRODUCT_DEFINE(sample_product, CONFIG_SAMPLE_USBD_PRODUCT);
IF_ENABLED(CONFIG_HWINFO, (USBD_DESC_SERIAL_NUMBER_DEFINE(sample_sn)));
```

在初始化 USB 设备之前，必须在运行时调用 `usbd_add_descriptor()` 将字符串描述符添加到设备上下文。

```c
err = usbd_add_descriptor(&sample_usbd, &sample_lang);
if (err) {
	LOG_ERR("Failed to initialize language descriptor (%d)", err);
	return NULL;
}

err = usbd_add_descriptor(&sample_usbd, &sample_mfr);
if (err) {
	LOG_ERR("Failed to initialize manufacturer descriptor (%d)", err);
	return NULL;
}

err = usbd_add_descriptor(&sample_usbd, &sample_product);
if (err) {
	LOG_ERR("Failed to initialize product descriptor (%d)", err);
	return NULL;
}

IF_ENABLED(CONFIG_HWINFO, (
	err = usbd_add_descriptor(&sample_usbd, &sample_sn);
))
if (err) {
	LOG_ERR("Failed to initialize SN descriptor (%d)", err);
	return NULL;
}
```

### 2.3.3\_创建各速率对应的配置

USB 设备对于每一种支持的速率至少需要一个**配置（Configuration）**实例。应用应使用 `USBD_CONFIGURATION_DEFINE` 实例化配置，随后再将 USB 设备功能分配给配置。

> 译注：配置是供主机选择的一套设备接口与功能组合。**全速（Full Speed，FS）**与**高速（High Speed，HS）**是 USB 的两种总线速率模式；为某模式声明配置不等于硬件自动具备该速率能力。

```c
static const uint8_t attributes = (IS_ENABLED(CONFIG_SAMPLE_USBD_SELF_POWERED) ?
				   USB_SCD_SELF_POWERED : 0) |
				  (IS_ENABLED(CONFIG_SAMPLE_USBD_REMOTE_WAKEUP) ?
				   USB_SCD_REMOTE_WAKEUP : 0);

/* Full speed configuration */
USBD_CONFIGURATION_DEFINE(sample_fs_config,
			  attributes,
			  CONFIG_SAMPLE_USBD_MAX_POWER, &fs_cfg_desc);

/* High speed configuration */
USBD_CONFIGURATION_DEFINE(sample_hs_config,
			  attributes,
			  CONFIG_SAMPLE_USBD_MAX_POWER, &hs_cfg_desc);
```

> 译注：这些是公共文件中的局部片段，`fs_cfg_desc`、`hs_cfg_desc` 等对象的定义需结合原文件阅读；不能仅拼接本页片段便认定是一份完整应用。

### 2.3.4\_将配置添加到上下文

对于特定速率的每个配置实例，必须在初始化 USB 设备之前，在运行时通过 `usbd_add_configuration()` 添加到上下文。注意使用 `USBD_SPEED_FS` 与 `USBD_SPEED_HS` 区分全速和高速。全速或高速的第一个配置，其 `bConfigurationValue` 为 1，此后的配置值依次递增。

```c
err = usbd_add_configuration(&sample_usbd, USBD_SPEED_FS,
			     &sample_fs_config);
if (err) {
	LOG_ERR("Failed to add Full-Speed configuration");
	return NULL;
}
```

### 2.3.5\_注册功能或类

完成前面的操作后，USB 设备仍没有功能。设备可以针对不同速率具有多个配置，各配置包含不同的功能集合。初始化设备之前，可以通过 `usbd_register_class()` 注册功能或类。使用 `USBD_SPEED_FS` 或 `USBD_SPEED_HS` 加上配置编号来指定目标配置。简单情况下，可通过 `usbd_register_all_classes()` 注册所有可用实例。

```c
err = usbd_register_all_classes(&sample_usbd, USBD_SPEED_FS, 1, blocklist);
if (err) {
	LOG_ERR("Failed to add register classes");
	return NULL;
}
```

### 2.3.6\_初始化设备

准备工作的最后一步是调用 `usbd_init()` 初始化设备。此后不能再修改设备配置。可以使用 `usbd_shutdown()` 撤销初始化，所有实例都可重用，但必须重复前述步骤。因此，可以关闭一个设备，注册另一种配置或功能，然后再次初始化。

在 USB 控制器层，`usbd_init()` 仅执行检测 **USB总线电源（Bus Power，信号名 VBUS）**变化所必需的操作。某些控制器只有在 VBUS 信号存在时才允许执行下一步。

功能或类的实现可能需要专用配置步骤，这些步骤应在初始化 USB 设备之前完成。

```c
err = usbd_init(&sample_usbd);
if (err) {
	LOG_ERR("Failed to initialize device support");
	return NULL;
}
```

### 2.3.7\_启用与禁用设备

启用 USB 设备的最后一步是调用 `usbd_enable()`。之后，如果设备已连接 USB 主机控制器，主机便可开始**枚举（Enumeration）**设备。应用可以通过 `usbd_disable()` 禁用 USB 设备。

> 译注：枚举是主机识别设备、读取描述符并选择配置的过程；应用完成设备栈初始化，与主机完成枚举，是两个不同阶段。

```c
ret = usbd_enable(sample_usbd);
if (ret) {
	LOG_ERR("Failed to enable device support");
	return ret;
}
```

> 译注：前面的 `sample_usbd` 是宏定义的上下文对象，示例调用传入 `&sample_usbd`；本段来自另一处使用上下文指针的调用位置，因此写作 `usbd_enable(sample_usbd)`。移植时必须依据变量实际类型传入 `struct usbd_context *`，不要混淆对象与指针。`usbd_disable()` 与撤销初始化的 `usbd_shutdown()` 也不是同一操作。

## 2.4\_USB消息通知

应用可以用 `usbd_msg_register_cb()` 注册回调，接收 USB 设备支持子系统的消息通知。多数消息描述通用设备状态变化，另有少数消息类型来自 USB CDC ACM 实现。

```c
err = usbd_msg_register_cb(&sample_usbd, msg_cb);
if (err) {
	LOG_ERR("Failed to register message callback");
	return NULL;
}
```

辅助函数 `usbd_msg_type_string()` 可将 `usbd_msg_type` 转换为人类可读的日志字符串。

如果控制器支持检测 VBUS 状态变化，电池供电应用可能希望仅在连接主机时启用 USB 设备。通用应用应调用 `usbd_can_detect_vbus()` 检查该能力。

```c
static void msg_cb(struct usbd_context *const usbd_ctx,
		   const struct usbd_msg *const msg)
{
	LOG_INF("USBD message: %s", usbd_msg_type_string(msg->type));

	if (msg->type == USBD_MSG_CONFIGURATION) {
		LOG_INF("\tConfiguration value %d", msg->status);
	}

	if (usbd_can_detect_vbus(usbd_ctx)) {
		if (msg->type == USBD_MSG_VBUS_READY) {
			if (usbd_enable(usbd_ctx)) {
				LOG_ERR("Failed to enable device support");
			}
		}

		if (msg->type == USBD_MSG_VBUS_REMOVED) {
			if (usbd_disable(usbd_ctx)) {
				LOG_ERR("Failed to disable device support");
			}
		}
	}
}
```

## 2.5\_内置功能

USB 设备栈内置多种 USB 功能。一些功能通过专用 API 供用户应用直接使用，例如 **人机接口设备（Human Interface Device，HID）**或**音频类（Audio Class）**设备；另一些功能使用通用 Zephyr **实时操作系统（Real-Time Operating System，RTOS）**驱动 API，例如 **大容量存储类（Mass Storage Class，MSC）**和**通信设备类（Communications Device Class，CDC）**实现。下表的标识字符串用于标识类或功能的第 `n` 个实例，并作为 `usbd_register_class()` 的参数。

> 译注：**设备类（Device Class）**规定一类设备向主机呈现的接口与行为。CDC 下的**抽象控制模型（Abstract Control Model，ACM）**用于本集的虚拟串口；**以太网控制模型（Ethernet Control Model，ECM）**用于以太网通信。**USB视频类（USB Video Class，UVC）**用于视频设备。HID 对应键盘、鼠标等交互设备，MSC 则向主机呈现存储介质。

| 类或功能 | 用户 API（如有） | 标识字符串 |
| --- | --- | --- |
| USB Audio 2 类 | [Audio Class 2 设备 API](P088_USB音频2设备API说明.md#uac2-device) | `uac2_n` |
| USB CDC ACM 类 | [UART 驱动 API](../hardware/P006_UART.md) | `cdc_acm_n` |
| USB CDC ECM 类 | 以太网设备 | `cdc_ecm_n` |
| USB 大容量存储类（MSC） | [USB MSC 设备 API](P057_USB大容量存储API说明.md#usbd-msc-device) | `msc_n` |
| USB 人机接口设备（HID） | [HID 设备 API](P041_新版HID设备API说明.md#usbd-hid-device) | `hid_n` |
| Bluetooth **主机控制器接口（Host Controller Interface，HCI）** USB 传输层 | [HCI RAW 通道](../bluetooth/P015_HCI原始通道.md#bt-hci-raw) | `bt_hci_n` |
| USB 视频类（UVC） | 视频设备 | `uvc_n` |

> 译注：这里的 `n` 是实例编号占位符，不是要求把字面值 `_n` 用作所有实例名称。具体宏、函数和消息枚举见 [USB 设备 API 参考](P015_USB设备核心API.md)与[消息 API 参考](P016_USB设备消息API.md)。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：USB文档入口](P001_USB文档入口.md) · [本模块主线目录](../reading/usb.md) · [全部主线](../reading/README.md) · [下一篇：USB_CDC_ACM](P003_USB_CDC_ACM.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：USB文档入口](P001_USB文档入口.md) · [下一章：USB CDC ACM](P003_USB_CDC_ACM.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
