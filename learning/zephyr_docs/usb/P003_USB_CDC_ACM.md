---
id: learning.zephyr-docs.usb.usb-cdc
title: USB_CDC_ACM
kind: reference
status: maintained
domains: [zephyr, usb]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/usb/device_next/cdc_acm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第3章\_USB_CDC_ACM

原文：[USB device CDC ACM](https://docs.zephyrproject.org/latest/services/connectivity/usb/device_next/cdc_acm.html)。读取日期：2026-10-12，`latest`。

**通用串行总线（Universal Serial Bus，USB）** 设备栈提供的 CDC ACM 功能属于**通信设备类（Communications Device Class，CDC）**，仅实现其中的**抽象控制模型（Abstract Control Model，ACM）**串口仿真，用途就是模拟串行线路。多数现代操作系统应能直接支持它，无须额外配置。

CDC ACM 在主机侧和设备侧都表现为串口，供用户或应用调用的接口是[通用异步收发器 UART 驱动 API](../hardware/P006_UART.md)。因此，已经使用 **通用异步收发器（Universal Asynchronous Receiver-Transmitter，UART）** **应用程序编程接口（Application Programming Interface，API）** 的应用，可以保留原有数据通信代码，通过补充配置并初始化 USB 设备栈，改用 CDC ACM 提供的串口。

## 3.1\_CDC_ACM_UART配置

与真实 UART 控制器一样，虚拟 CDC ACM UART 也通过设备树描述，其 `compatible` 属性为 [zephyr,cdc-acm-uart](../uart_ti_wch_virtual_binding_reference/P012_zephyr_cdc-acm-uart.md#std-dtcompatible-zephyr-cdc-acm-uart)。

启用 USB 设备支持，并在设备树源文件中提供相应兼容节点后，会自动选中 CDC ACM 支持。必要时，可以通过 Kconfig 配置项 `CONFIG_USBD_CDC_ACM_CLASS` 显式禁用它。可创建的 CDC ACM 实例数量取决于 USB 设备控制器支持的**端点（Endpoint）**数量。每个实例需要三个端点：两个**批量端点（Bulk Endpoint）**，即一个 IN、一个 OUT，以及一个 `MaxPacketSize` 为 16 的**中断 IN 端点（Interrupt IN Endpoint）**。

> 译注：端点是设备中收发 USB 数据的逻辑通信端口。方向以主机为参照：IN 表示设备向主机发送，OUT 表示主机向设备发送；这里的“中断端点”是 USB 传输类型，不等同于处理器的中断向量。

CDC ACM 节点可用 `label` 属性区分主机侧的不同接口。设备树覆盖文件示例：

```devicetree
&zephyr_udc0 {
        cdc_acm_uart0: cdc_acm_uart0 {
                compatible = "zephyr,cdc-acm-uart";
                label = "CDC_ACM_0";
        };
};
```

应用在使用 CDC ACM UART 前，可能希望等待 **数据终端就绪（Data Terminal Ready，DTR）**信号；具体实现参见 [USB CDC ACM UART 示例](P054_CDCACM串口示例.md#usb-cdc-acm)。

> 原文注意：为了与主机通信，除 UART 配置外，应用还必须启用 USB 设备栈。请参阅[配置并启用USB设备支持](P002_USB设备支持.md)，并仔细阅读下一节。对于从旧版设备栈迁移的用户和应用，这是需要适配的部分。

## 3.2\_将CDC_ACM_UART用作串行后端

结合上例和 `chosen` 节点中的 `zephyr,console` 属性，可将 CDC ACM UART 配置为控制台设备。

```devicetree
/ {
        chosen {
                zephyr,console = &cdc_acm_uart0;
        };
};

&zephyr_udc0 {
        cdc_acm_uart0: cdc_acm_uart0 {
                compatible = "zephyr,cdc-acm-uart";
                label = "CDC_ACM_0";
        };
};
```

同样，可以用 `chosen` 节点的 `zephyr,shell-uart` 属性，让 shell 使用 CDC ACM UART 作为串行后端。参见[自定义 Shell 模块示例](https://docs.zephyrproject.org/latest/samples/subsys/shell/shell_module/README.html#shell-module)和 [chosen 节点文档](https://docs.zephyrproject.org/latest/build/dts/api/api.html#devicetree-chosen-nodes)。

串行后端是很常见的用途，而且 CDC ACM UART 不需要运行时配置，因此设备栈提供了辅助机制，执行[设备配置与启用](P002_USB设备支持.md)中的步骤。启用 `CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT` 后，该机制会用一个 CDC ACM 实例初始化 USB 设备栈。[USB CDC ACM 控制台示例](P055_CDCACM控制台示例.md#usb-cdc-acm-console)演示其用法。

像 [nRF52840 Dongle](https://docs.zephyrproject.org/latest/boards/nordic/nrf52840dongle/doc/index.html#nrf52840dongle)这样没有调试适配器、但有 USB 设备控制器，并希望用 CDC ACM UART 作为日志与 shell 默认串行后端的开发板，也应使用 `CONFIG_CDC_ACM_SERIAL_INITIALIZE_AT_BOOT`。由于这类配置对不同开发板是相同的，项目提供了公共[设备树文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/common/usb/cdc_acm_serial.dtsi)和 [Kconfig 文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/common/usb/Kconfig.cdc_acm_serial.defconfig)，分别纳入开发板设备树和 `Kconfig.defconfig`。

## 3.3\_在应用中使用CDC_ACM_UART

CDC ACM 实现虚拟 UART 控制器，提供**中断驱动接口（Interrupt-driven API）**和**轮询接口（Polling API）**，目前不支持**异步接口（Asynchronous API，代码中简称 ASYNC）**。应用通过 CDC ACM UART 通信时，优先使用中断驱动 API。必须理解 UART API 文档；以下说明其中需要注意的地方。

### 3.3.1\_中断驱动UART_API

原文说明 CDC ACM UART 内部使用两个**环形缓冲区（Ring Buffer）**，承担中断驱动 API 中**发送（Transmit，TX）**与**接收（Receive，RX）**的**先进先出（First In, First Out，FIFO）**缓冲区职责。

按照中断驱动 API 的要求，`uart_irq_update()`、`uart_irq_is_pending()`、`uart_irq_rx_ready()`、`uart_irq_tx_ready()`、`uart_fifo_read()` 和 `uart_fifo_fill()` 应在中断处理回调中调用，回调通过 `uart_irq_callback_user_data_set()` 注册。为了避免未定义行为，这些函数的实现会检查调用上下文；若不在要求的处理上下文中，会调用失败。

> 译注：原文用“interrupt handler”描述 UART 回调，不代表虚拟 CDC ACM 一定运行在 **中央处理器（Central Processing Unit，CPU）** 硬件中断上下文。本地 `subsys/usb/device_next/class/usbd_cdc_acm.c` 实际通过工作队列执行回调并检查工作队列上下文；RX 侧还使用 `net_buf` FIFO，而非与 TX 完全相同的环形缓冲区。该本地源码与官网 `latest` 不自动视为同一快照。应用应在驱动调用的已注册回调中使用这些接口，不要从任意线程或任意硬件 **中断服务例程（Interrupt Service Routine，ISR）** 调用，也不要依赖缓冲区的私有实现。

UART API 还要求：必须先调用 `uart_irq_update()`，再调用 `uart_irq_is_pending()`、`uart_irq_rx_ready()` 或 `uart_irq_tx_ready()`。

简化后的应用中断处理回调如下：

```c
static void interrupt_handler(const struct device *dev, void *user_data)
{
        while (true) {
                uart_irq_update(dev);

                if (uart_irq_is_pending(dev) <= 0) {
                        break;
                }

                if (uart_irq_rx_ready(dev)) {
                        int len;
                        int n;

                        /* ... */
                        n = uart_fifo_read(dev, buffer, len);
                        /* ... */
                }

                if (uart_irq_tx_ready(dev)) {
                        int len;
                        int n;

                        /* ... */
                        n = uart_fifo_fill(dev, buffer, len);
                  /* ... */
                }
        }
}
```

> 译注：这只是流程框架。`buffer`、有效长度和收发处理被省略，`len` 尚未赋值；不能直接当作可运行代码。应用应根据实际返回数量推进缓冲区，在没有待发数据时关闭 TX 中断请求，并及时取走 RX 数据，避免一直保持 ready 状态而空转。

这些函数并不直接依赖 USB 设备状态。填充 TX FIFO 不代表数据正在发送给主机；成功读取 RX FIFO 也不代表设备仍与主机连接。只要 TX FIFO 有空间且 TX 中断已启用，`uart_irq_tx_ready()` 就会成功；只要 RX FIFO 有数据且 RX 中断已启用，`uart_irq_rx_ready()` 就会成功。`uart_irq_tx_complete()` 尚未实现。

完整接口见 [UART 中断驱动 API](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interrupt.html)。

### 3.3.2\_轮询UART_API

CDC ACM 的轮询输出实现遵循轮询 API。仅在启用了 `hw-flow-control` 属性，并且从非 ISR 上下文调用时，才会在 TX FIFO 已满的情况下阻塞。

> 译注：这里的 `hw-flow-control` 是虚拟 UART 对阻塞行为的配置，不能据其名称推断板上有物理 RTS/CTS 引脚。原文限定了“何时阻塞”，不构成断线或缓冲区满时数据必达的保证。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：USB设备支持](P002_USB设备支持.md) · [本模块主线目录](../reading/usb.md) · [全部主线](../reading/README.md) · [下一篇：USB厂商与产品标识](P004_USB厂商与产品标识.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：USB设备支持](P002_USB设备支持.md) · [下一章：USB厂商与产品标识](P004_USB厂商与产品标识.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
