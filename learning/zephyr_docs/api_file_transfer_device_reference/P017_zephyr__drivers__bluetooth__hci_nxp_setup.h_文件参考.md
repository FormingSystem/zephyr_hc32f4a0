---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-17
title: zephyr__drivers__bluetooth__hci_nxp_setup.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hci__nxp__setup_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_drivers\_\_bluetooth\_\_hci\_nxp\_setup.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hci__nxp__setup_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP HCI扩展API（Extended API）。

<a id="details"></a>

```c
#include <zephyr/device.h>
```

查看此文件的源码。

NXP HCI扩展API（Extended API）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.1\_函数（Functions）

<a id="r_ab07ac59e57ce5a1c59aa6f5c07c6bd73"></a>

```c
int bt_nxp_trigger_ir (const struct device *dev)
```

相关声明：[bt_nxp_trigger_ir](#ab07ac59e57ce5a1c59aa6f5c07c6bd73)、[device](../device_reference/P002_设备对象结构.md)。

触发 NXP 蓝牙控制器（Bluetooth Controller）的独立复位（Independent Reset，IR）。

## 17.2\_详细说明（Detailed Documentation）

<a id="ab07ac59e57ce5a1c59aa6f5c07c6bd73"></a>

### `bt_nxp_trigger_ir()`

```c
int bt_nxp_trigger_ir ( const struct device * dev)
```

触发 NXP 蓝牙控制器（Bluetooth Controller）的独立复位（Independent Reset，IR）。

本函数在 NXP 蓝牙控制器上启动独立复位（Independent Reset）序列。独立复位允许在不执行整个系统复位的情况下复位并重新初始化蓝牙控制器。触发 IR 后，将向控制器重新下载固件（Firmware）。

使用示例：

原始示例（Example）：

```c
int err;

// Step 1: Disable Bluetooth stack
err = bt_disable();
if (err) {
    LOG_ERR("Failed to disable Bluetooth: %d", err);
    return err;
}

// Step 2: Trigger Independent Reset
err = bt_nxp_trigger_ir(uart_dev);
if (err) {
    LOG_ERR("Failed to trigger IR: %d", err);
    return err;
}

// Step 3: Re-enable Bluetooth stack
err = bt_enable(NULL);
if (err) {
    LOG_ERR("Failed to re-enable Bluetooth: %d", err);
    return err;
}
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向用于 HCI 通信的 UART 设备结构体（Device Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EAGAIN` | 蓝牙（Bluetooth）尚未禁用时。调用本函数之前，请使用 `bt_disable()` 禁用蓝牙。 |
| `-ENODEV` | UART 设备未就绪，或未启用此功能时。 |
| `-EIO` | 触发独立复位（IR）之后固件下载（Firmware Download）失败时。 |
| `other` | 其他失败返回负错误码（Negative Error Code）。 |

**说明（Note）**：**注意（Note）：**仅在启用 `CONFIG_HCI_NXP_CONFIG_IR` 时提供此 API。

**说明（Note）**：**前置条件（Precondition）：**调用本函数之前必须禁用蓝牙。在触发独立复位（IR）之前，使用 `bt_disable()` 禁用蓝牙协议栈（Bluetooth Stack）。未禁用蓝牙会使本函数返回 `-EAGAIN`。

**说明（Note）**：**后置条件（Postcondition）：**成功完成后，蓝牙控制器已经复位，固件已重新下载。应用必须调用 `bt_enable()` 重新激活蓝牙接口（Bluetooth Interface）。


## 17.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P310_hci_nxp_setup.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [CONFIG_HCI_NXP_CONFIG_IR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HCI_NXP_CONFIG_IR)
- [bt_disable()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga0a58e5a050170e84a80f8d5bb3516ec7)
- [bt_enable()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac45d16bfe21c3c38e834c293e5ebc42b)
- [LOG_ERR](../log_core_reference/P002_日志公共接口.md#gad6db28c61c838c1f7316417e1e4847f2)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="agroup__bt__gap_html_ga0a58e5a050170e84a80f8d5bb3516ec7"></a>
<a id="agroup__bt__gap_html_gac45d16bfe21c3c38e834c293e5ebc42b"></a>
<a id="agroup__log__api_html_gad6db28c61c838c1f7316417e1e4847f2"></a>
<a id="ahci__nxp__setup_8h_html_ab07ac59e57ce5a1c59aa6f5c07c6bd73"></a>

---

[上一章](P016_zephyr__drivers__interrupt_controller__gd32_exti.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P018_zephyr__dt-bindings__interrupt-controller__intel-ioapic.h_文件参考.md)
