---
id: learning.zephyr-docs.usb.page-8
title: 旧版USB设备支持
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/usb/device/usb_device.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_旧版USB设备支持

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/usb/device/usb_device.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 8.1\_概述

旧版 USB 设备栈在 USB 设备控制器驱动与 USB 设备类驱动或用户应用之间提供独立于硬件的接口。它移植自 LPCUSB 设备栈，并在后续发展中持续修改和扩展，提供以下功能：

- 通过控制器驱动提供的[USB 设备控制器驱动 API（已弃用）](P128_旧版USB设备控制器API.md#usb-dc-api)与 USB 设备控制器交互。
- 响应标准设备请求、返回标准描述符，实质上处理 USB 2.0 规范第 9 章的内容，尤其是表 9-3 中的标准设备请求。
- 为 USB 设备类或用户应用提供编程接口，定义见[include/zephyr/usb/usb_device.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/usb/usb_device.h)。

**原文注意：**[旧版 USB 设备支持 API](P127_旧版USB设备API入口.md#usb-api)中列出的全部 API 及依赖它们的功能均已弃用，原文计划在 v4.5.0 移除。请使用[新版 USB 设备支持 API](P013_USB设备API目录.md#usb-device-next-api)所代表的新实现。

> 译注：弃用与计划移除时间按保存的官方页面翻译。当前是否仍保留某项实现，应以所用 Zephyr 版本为准，不能把文档计划当作已执行删除的证明。本章用于理解旧代码；新版设备栈的上下文、描述符、类注册与启用方式见[USB设备支持](P002_USB设备支持.md)，两套接口不应混用。

## 8.2\_支持的USB设备类

### 8.2.1\_音频

音频类（Audio Class）有一个实验性实现，遵循 1.00 版规范（`bcdADC 0x0100`），仅支持同步型同步方式（Synchronous Synchronization Type）。参见[旧版 USB 音频麦克风与耳机](P139_旧版USB麦克风与耳机示例.md#usb-audio-headphones-microphone)和[旧版 USB 音频耳麦](P138_旧版USB音频耳麦示例.md#usb-audio-headset)示例。

### 8.2.2\_蓝牙HCI的USB传输层

蓝牙主机控制器接口（Host Controller Interface，HCI）的 USB 传输层使用[HCI RAW 通道](../bluetooth/P015_HCI原始通道.md#bt-hci-raw)向宿主暴露 HCI 接口。其实现并未完全遵循蓝牙规范的描述，只包含一个接口，端点配置为：

- HCI 命令通过控制端点（Control Endpoint）传输，只支持主机到设备方向。
- HCI 事件通过中断 IN 端点（Interrupt IN Endpoint）传输。
- 异步无连接（Asynchronous Connection-Less，ACL）数据通过一个批量 IN 和一个批量 OUT 端点传输。

由于此处[蓝牙支持](../bluetooth/P001_蓝牙概览.md#bluetooth)未支持相应类型，用于语音通道的第二个接口尚未实现。在 Linux 上，如果 HCI USB 是配置中唯一的接口，问题通常不大：`btusb` 驱动不会尝试占用第二个等时接口（Isochronous Interface）。但如果 HCI USB 在复合配置（Composite Configuration）中是第一个接口，Linux 的 `btusb` 驱动会占用第一个及紧随其后的接口，导致其他复合功能无法工作。因此，这一旧版 HCI USB 不应用于复合配置。新版 USB 支持的实现已修复此问题。

参见[HCI USB](P190_蓝牙HCIUSB控制器示例.md#bluetooth_hci_usb)示例。

### 8.2.3\_CDC ACM

通信设备类／抽象控制模型（Communications Device Class / Abstract Control Model，CDC ACM）可作为 Zephyr 多种子系统的后端，但初次接触时配置并不简单。下面说明不同使用场景及常见问题。

CDC ACM 向使用者提供[通用异步收发器（Universal Asynchronous Receiver-Transmitter，UART）驱动 API](../hardware/P006_UART.md#uart-api)。它与真实 UART 控制器有以下重要行为差异：

- 只有 USB 设备栈完成初始化并启动后才能传输数据，此前的数据都会被丢弃。
- 即使设备已连接到主机，也仍需要主机端应用请求数据。
- CDC ACM 的轮询输出（poll out）实现遵循该 API：只有启用了 `hw-flow-control` 属性，且调用来自非中断服务程序（Interrupt Service Routine，ISR）上下文时，才会在发送环形缓冲区（TX Ring Buffer）已满时阻塞。

CDC ACM UART 的设备树兼容标识是[zephyr,cdc-acm-uart](../uart_ti_wch_virtual_binding_reference/P012_zephyr_cdc-acm-uart.md#std-dtcompatible-zephyr-cdc-acm-uart)。启用 USB 设备支持且设备树中存在匹配节点时，会自动选择 CDC ACM 支持；必要时可以用 [`CONFIG_USB_CDC_ACM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_CDC_ACM) 显式禁用。可定义和使用的 CDC ACM UART 实例数量大约为四个，具体受控制器支持的最大端点数量限制。

CDC ACM UART 节点应是 USB 设备控制器节点的子节点。控制器节点名称因厂商而异，为使应用和示例尽量通用，默认 USB 设备控制器通常带有 `zephyr_udc0` 节点标签。CDC ACM UART 常在设备树覆盖文件中描述，如下：

```dts
&zephyr_udc0 {
        cdc_acm_uart0: cdc_acm_uart0 {
                compatible = "zephyr,cdc-acm-uart";
                label = "CDC_ACM_0";
        };
};
```

[USB CDC ACM UART 示例](P054_CDCACM串口示例.md#usb-cdc-acm)具有类似的覆盖文件。虽然没有特别的属性，用设备树描述它看起来似乎有些繁琐，但这样做是为了让应用容易在真实 UART 控制器与 CDC ACM UART 之间切换。

#### (1)\_通过CDC ACM UART使用控制台

结合上面的 CDC ACM UART 节点与 `chosen` 节点的 `zephyr,console` 属性，可指定控制台使用 CDC ACM UART。[USB CDC ACM 控制台](P055_CDCACM控制台示例.md#usb-cdc-acm-console)示例使用了类似覆盖文件。

```dts
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

建议应用在使用控制台前，先等待数据终端就绪（Data Terminal Ready，DTR）信号：

```c
const struct device *const dev = DEVICE_DT_GET(DT_CHOSEN(zephyr_console));
uint32_t dtr = 0;

if (usb_enable(NULL)) {
        return;
}

while (!dtr) {
        uart_line_ctrl_get(dev, UART_LINE_CTRL_DTR, &dtr);
        k_sleep(K_MSEC(100));
}

printk("nuqneH\n");
```

#### (2)\_将CDC ACM UART作为后端

与控制台示例相同，也可通过设置[chosen 节点](https://docs.zephyrproject.org/latest/build/dts/api/api.html#devicetree-chosen-nodes)属性，将 CDC ACM UART 配置为其他子系统的后端。

可用于选择 CDC ACM UART 后端的部分 Zephyr 专用属性如下：

- `zephyr,bt-c2h-uart`：用于蓝牙，参见[HCI UART](../bluetooth_samples/P016_HCI_UART传输.md#bluetooth_hci_uart)。
- `zephyr,ot-uart`：用于 OpenThread，参见[OpenThread 协处理器](../networking/P175_OpenThread协处理器.md#openthread-coprocessor)。
- `zephyr,shell-uart`：用于 Shell 串口后端，参见[samples/subsys/shell/shell_module](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/shell/shell_module)。
- `zephyr,uart-mcumgr`：用于[SMP 服务器](../firmware_update/P022_SMP服务器示例.md#smp-svr)示例。

#### (3)\_缓解POSIX终端默认回显问题

Linux 等 POSIX 系统默认对 tty 终端设备启用 `ECHO` 回显。如果不需要回显，宿主应用可先 `open()` 打开 tty，再通过 `ioctl()` 关闭回显，优先使用 `tcsetattr()`。但 `open()` 与 `ioctl()` 之间存在固有竞态：回显仍开启时，任何收到的字符都会被回送，即使宿主应用没有调用 `read()`。当 CDC ACM 另一侧没有真实 UART 时，这个问题尤其明显，因为没有波特率带来的传输延迟。

为缓解这一问题，Zephyr 的 CDC ACM 实现在设备配置完成后，向 IN 端点提交零长度包（Zero-Length Packet，ZLP）。主机读取 ZLP 是宿主应用已打开 tty 的一个较可靠迹象；随后 Zephyr 在发送实际载荷前强制等待 [`CONFIG_CDC_ACM_TX_DELAY_MS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CDC_ACM_TX_DELAY_MS) 毫秒，为首次且仅首次打开 tty 的应用留出关闭回显的时间。如果完全不希望该 CDC ACM 设备启用回显，最好配置 udev 规则，在设备连接时就关闭回显。

CDC ACM 用于 Zephyr Shell 时尤其不希望回显：设置颜色的控制字符被送回 Shell 后，会被解释为无效命令，使读者看到乱码。虽然 minicom 默认关闭回显，但以“退出并复位”方式退出时，会将 termios 设置恢复为进入前的状态。如果 minicom 是第一个打开 tty 的应用，这种退出方式会重新开启回显，为下一个应用留下问题，Zephyr 设备侧已无法缓解。建议不复位地退出 minicom，或者在启动 minicom 之前先关闭回显。

### 8.2.4\_DFU

USB 设备固件升级（Device Firmware Upgrade，DFU）类实现与[设备固件升级](../firmware_update/P002_设备固件升级.md#dfu)及[MCUBoot API](../firmware_update/P002_设备固件升级.md#mcuboot-api)紧密耦合，因此目标平台必须支持[Flash 镜像 API](../firmware_update/P002_设备固件升级.md#flash-img-api)。

参见[旧版 USB DFU 示例](P133_旧版USB固件升级示例.md#legacy-usb-dfu)。

### 8.2.5\_人机接口设备支持

人机接口设备（Human Interface Device，HID）支持借用[设备驱动模型](../hardware/P003_设备驱动模型.md#device-model-api)，目的仅是让应用能调用 [`device_get_binding()`](../device_reference/P001_设备模型公共接口.md#ga15386ca9ab38f3e30183c18f604fa835)。这里并没有通常意义上的 HID 设备 API，实际接口由 [`hid_ops`](P047_旧版HID回调接口.md) 提供。默认实例名为 `HID_n`，其中 `n` 根据 [`CONFIG_USB_HID_DEVICE_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_HID_DEVICE_COUNT) 可为 0、1、2……。

每个 HID 实例都需要 HID 报告描述符（Report Descriptor）；与核心交互的接口和报告描述符必须通过 [`usb_hid_register_device()`](P046_旧版HID设备接口API.md#ga8b08b633472ceb1323f09ef81176520f) 注册。

由于 USB HID 规范也供 USB 子系统之外使用，API 参考分为[通用 HID 支持](P040_HID通用说明.md#usb-hid-common)与[USB HID 类 API（已弃用）](P044_旧版HID类API说明.md#usb-hid-device)两部分。应使用通用 HID 支持中的辅助宏构造报告描述符，宏名与 USB HID 规范中的名称对应。

HID 类接口的每个实例都需要一个中断 IN 端点，中断 OUT 端点可选。因此，[`hid_ops`](P047_旧版HID回调接口.md) 的最低实现要求是提供 `int_in_ready` 回调。

```c
#define REPORT_ID               1
static bool configured;
static const struct device *hdev;

static void int_in_ready_cb(const struct device *dev)
{
        static uint8_t report[2] = {REPORT_ID, 0};

        if (hid_int_ep_write(hdev, report, sizeof(report), NULL)) {
                LOG_ERR("Failed to submit report");
        } else {
                report[1]++;
        }
}

static void status_cb(enum usb_dc_status_code status, const uint8_t *param)
{
        if (status == USB_DC_RESET) {
                configured = false;
        }

        if (status == USB_DC_CONFIGURED && !configured) {
                int_in_ready_cb(hdev);
                configured = true;
        }
}

static const uint8_t hid_report_desc[] = {
        HID_USAGE_PAGE(HID_USAGE_GEN_DESKTOP),
        HID_USAGE(HID_USAGE_GEN_DESKTOP_UNDEFINED),
        HID_COLLECTION(HID_COLLECTION_APPLICATION),
        HID_LOGICAL_MIN8(0x00),
        HID_LOGICAL_MAX16(0xFF, 0x00),
        HID_REPORT_ID(REPORT_ID),
        HID_REPORT_SIZE(8),
        HID_REPORT_COUNT(1),
        HID_USAGE(HID_USAGE_GEN_DESKTOP_UNDEFINED),
        HID_INPUT(0x02),
        HID_END_COLLECTION,
};

static const struct hid_ops my_ops = {
        .int_in_ready = int_in_ready_cb,
};

int main(void)
{
        int ret;

        hdev = device_get_binding("HID_0");
        if (hdev == NULL) {
                return -ENODEV;
        }

        usb_hid_register_device(hdev, hid_report_desc, sizeof(hid_report_desc),
                                &my_ops);

        ret = usb_hid_init(hdev);
        if (ret) {
                return ret;
        }

        return usb_enable(status_cb);
}
```

如果应用希望通过中断 OUT 端点接收输出报告，必须启用 [`CONFIG_ENABLE_HID_INT_OUT_EP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENABLE_HID_INT_OUT_EP) 并提供 `int_out_ready` 回调。这种设计的缺点是，[`CONFIG_ENABLE_HID_INT_OUT_EP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENABLE_HID_INT_OUT_EP)、[`CONFIG_HID_INTERRUPT_EP_MPS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HID_INTERRUPT_EP_MPS) 等 Kconfig 选项会作用于全部实例。原文指出，此设计问题将在新版 USB 支持的 HID 类实现中修正。

参见[USB HID 鼠标](P052_HID鼠标示例.md#usb-hid-mouse)示例。

### 8.2.6\_大容量存储类

大容量存储类（Mass Storage Class，MSC）遵循仅批量传输（Bulk-Only Transport，BOT）规范，使用[磁盘访问接口](../storage/P008_磁盘访问.md#disk-access-api)访问并向主机暴露 RAM 磁盘、Flash 分区上的模拟块设备或 SD 卡。同一时间只能导出一个磁盘实例。

使用的磁盘由 [`CONFIG_MASS_STORAGE_DISK_NAME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MASS_STORAGE_DISK_NAME) 指定，应与应用希望暴露给主机的磁盘访问驱动所使用的名称一致。Flash、RAM、SDMMC/MMC 磁盘驱动通过节点属性 `disk-name` 设置磁盘名。

对 Flash 分区上的模拟块设备，必须在设备树中描述所用 Flash 分区和 Flash 磁盘。如果开发板层已描述存储分区，应用覆盖文件还须先删除 `storage_partition` 节点；[`CONFIG_MASS_STORAGE_DISK_NAME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MASS_STORAGE_DISK_NAME) 应与 `disk-name` 相同。

```dts
/delete-node/ &storage_partition;

&mx25r64 {
        partitions {
                compatible = "fixed-partitions";
                #address-cells = <1>;
                #size-cells = <1>;

                storage_partition: partition@0 {
                        label = "storage";
                        reg = <0x00000000 0x00020000>;
                };
        };
};

/ {
        msc_disk0 {
                compatible = "zephyr,flash-disk";
                partition = <&storage_partition>;
                disk-name = "NAND";
                cache-size = <4096>;
        };
};
```

磁盘名称属性（`disk-property`）中的 `NAND` 可能令人困惑，但这里只是某些文件系统识别磁盘的名称。因此，如果应用也要访问所导出磁盘上的文件系统，应使用默认名称，参见[USB 大容量存储](P060_USB大容量存储示例.md#usb-mass)示例。

> 译注：`/delete-node/` 是设备树语法，不是删除磁盘文件的命令；上述 Flash 分区布局属于官方示例。名称为 `NAND` 也不能证明底层实际器件就是 NAND Flash。

### 8.2.7\_网络

以下三种实现以相似方式，在远端 USB 主机与 Zephyr 网络支持之间提供虚拟以太网连接：

- CDC 以太网控制模型（Ethernet Control Model，ECM），通过 [`CONFIG_USB_DEVICE_NETWORK_ECM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_NETWORK_ECM) 启用。
- CDC 以太网仿真模型（Ethernet Emulation Model，EEM），通过 [`CONFIG_USB_DEVICE_NETWORK_EEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_NETWORK_EEM) 启用。
- 远程网络驱动接口规范（Remote Network Driver Interface Specification，RNDIS）支持，通过 [`CONFIG_USB_DEVICE_NETWORK_RNDIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_NETWORK_RNDIS) 启用。

参见[旧版 USB 设备 netusb 示例](P136_旧版USB网络设备示例.md#legacy-netusb)。

使用 RNDIS 的应用应启用 [`CONFIG_USB_DEVICE_OS_DESC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_OS_DESC)，以改善 Microsoft Windows 宿主上的使用体验。

## 8.3\_二进制设备对象存储支持

可通过 [`CONFIG_USB_DEVICE_BOS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_BOS) 启用二进制设备对象存储（Binary Device Object Store，BOS）处理。这还会将设备描述符的 `bcdUSB` 改为 `0210`。应用应调用 [`usb_bos_register_cap()`](P155_旧版USB设备栈核心API.md#ga1bf8ec88cf752e98234d9f8bb57f976a) 注册能力描述符（Capability Descriptor）等描述符；已注册的描述符会加入 BOS 根描述符并由协议栈处理。

参见[旧版 WebUSB](P140_旧版WebUSB示例.md#legacy-webusb)示例。

## 8.4\_接口号与端点地址的分配

在 USB 术语中，功能（function）指向主机提供某种能力的设备，例如实现键盘的 HID 类设备。一个功能包含一组接口（interfaces），至少需要一个接口。接口可以包含设备端点（endpoints）：例如 HID 类设备至少需要一个输入端点，而 USB DFU 类不需要额外的设备端点。组合多个功能的 USB 设备称为多功能 USB 设备，例如同时提供 HID 和 CDC ACM。

> 译注：DFU“不需要端点”针对功能接口的非控制端点；默认控制端点 0 仍承担控制请求。

Zephyr 的 USB 支持允许组合内置 USB 类／功能与用户自定义实现，主要限制是可用设备端点数量。每个设备端点都有唯一地址，由方向与四位端点编号共同组成。编号 0 用作设备初始化和配置的默认控制通道；规范还允许功能最多使用 `15 IN` 和 `15 OUT`，即 15 个 IN 与 15 个 OUT 端点，实际数量取决于设备控制器。

并非每个控制器都支持最多数量及所有端点类型。例如，某控制器可能只在端点编号 8 上支持一个等时 IN 与一个等时 OUT 端点，对应地址 `0x88` 和 `0x08`。有的控制器允许同一编号同时用于 IN／OUT，例如中断 IN `0x81` 与批量 OUT `0x01`；另一些控制器则每个编号只能处理一个端点。接口、接口专用及端点描述符向主机提供接口数量、接口关联、端点类型和地址等信息。

特定功能的主机驱动通过接口和端点描述符取得地址、类型及其他属性，因此可以通用地工作。例如，设备可组合一个或多个 CDC ACM 与一个或多个 CDC ECM 类实现，无需为这种组合提供专用驱动。

Zephyr 内置 USB 类／功能的接口和端点描述符通常按递增顺序给出默认接口号与端点地址。初始化时，默认接口号可根据当前配置中的接口数量重新分配。端点地址则依据控制器能力以及配置中的接口数量重新分配，因为不是所有控制器都支持任意端点组合。因此，设备侧类／功能也必须在运行时检查实际描述符中的值。这种机制让通用及多功能示例主要受控制器资源限制，例如端点数和端点先进先出缓冲区（First-In, First-Out，FIFO）的容量。

有些特定功能的主机驱动，例如 Linux 内核中的某些驱动，不读取描述符以确定接口号和端点地址，而使用硬编码值。这样的驱动不能通用于不同设备控制器、不同设备配置以及与其他功能的组合。它也可能原本就是为特定硬件设计，而无意支持该硬件的兼容实现。相反，如果驱动应具备通用性并支持不同硬件变体，就不能硬编码接口号和端点地址。

Zephyr 无法禁用端点重新分配，这可能使某些硬件兼容固件难以实现。可行时，应修改主机驱动，从接口和端点描述符读取实际值。

## 8.5\_在native\_sim中通过USBIP测试

通过 USBIP 实现的虚拟 USB 控制器可用于测试设备栈。按一般构建流程，为[native_sim](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim)配置构建 USB 示例。

运行已构建的示例：

```bash
west build -t run
```

在另一个终端列出 USB 设备：

```console
$ usbip list -r localhost
Exportable USB devices
======================
 - 127.0.0.1
        1-1: unknown vendor : unknown product (2fe3:0100)
           : /sys/devices/pci0000:00/0000:00:01.2/usb1/1-1
           : (Defined at Interface level) (00/00/00)
           :  0 - Vendor Specific Class / unknown subclass / unknown protocol (ff/00/00)
```

在终端执行以下命令连接 USB 设备：

```console
$ sudo usbip attach -r localhost -b 1-1
```

此时设备应已接入 Linux 宿主，可通过以下命令检查：

```console
$ sudo usbip port
Imported USB devices
====================
Port 00: <Port in Use> at Full Speed(12Mbps)
       unknown vendor : unknown product (2fe3:0100)
       7-1 -> usbip://localhost:3240/1-1
           -> remote bus/dev 001/002
$ lsusb -d 2fe3:0100
Bus 007 Device 004: ID 2fe3:0100
```

> 译注：这里保留的是旧版设备控制器路线及原文预期输出。先完成对应示例的构建，`west build -t run` 才能运行；Linux 宿主还需具备 USB/IP 工具与模块。`$` 为提示符，设备号和系统路径是输出内容，不是应照抄创建的仓库路径。新版主机导出路线见[USB/IP协议支持](P006_USBIP协议支持.md)。本批没有执行这些测试。

## 8.6\_USB厂商标识与产品标识

Zephyr 项目的 USB 厂商标识（Vendor ID，VID）为 `0x2FE3`。厂商把 Zephyr USB 设备支持集成到自身产品时，**不得使用这个 VID**。

每个 USB [示例](P065_USB示例目录.md#usb)具有独立的产品标识（Product ID，PID）。如果已指定 USB 维护者，由该维护者分配其他 PID；否则由 Zephyr 技术指导委员会（Technical Steering Committee）依据理由充分且有文档记录的申请分配。

原页列出的已使用 PID 如下：

| 示例 | PID |
| --- | --- |
| [USB CDC ACM UART 示例](P054_CDCACM串口示例.md#usb-cdc-acm) | `0x0001` |
| 保留，原用于 `usb-cdc-acm-composite` | `0x0002` |
| 保留，原用于 `usb-hid-cdc` | `0x0003` |
| [USB CDC ACM 控制台](P055_CDCACM控制台示例.md#usb-cdc-acm-console) | `0x0004` |
| [USB DFU](P064_USB设备固件升级示例.md#usb-dfu)，运行时模式（Run-Time） | `0x0005` |
| 保留，原用于 `usb-hid` | `0x0006` |
| [USB HID 鼠标](P052_HID鼠标示例.md#usb-hid-mouse) | `0x0007` |
| [USB 大容量存储](P060_USB大容量存储示例.md#usb-mass) | `0x0008` |
| [USB 设备测试应用](P067_USB设备测试示例.md#testusb-app) | `0x0009` |
| [WebUSB](P069_WebUSB示例.md#webusb) | `0x000A` |
| [HCI USB](P190_蓝牙HCIUSB控制器示例.md#bluetooth_hci_usb) | `0x000B` |
| 保留，原用于 `bluetooth_hci_usb_h4` | `0x000C` |
| 保留，原用于 `wpan-usb` | `0x000D` |
| [USB 音频异步显式反馈示例](P091_USB音频显式反馈示例.md#uac2-explicit-feedback) | `0x000E` |
| [USB 音频异步隐式反馈示例](P092_USB音频隐式反馈示例.md#uac2-implicit-feedback) | `0x000F` |
| [USB 视频摄像头](P124_USB视频摄像头示例.md#uvc) | `0x0011` |
| [USB DFU](P064_USB设备固件升级示例.md#usb-dfu)，DFU 模式（DFU Mode） | `0xFFFF` |

USB 设备描述符字段 `bcdDevice`（设备发行号，Device Release Number）以二进制编码十进制（Binary Coded Decimal，BCD）表示 Zephyr 内核的主、次版本号。


译注核对来源：[include/zephyr/usb/usb_device.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usb_device.h)、[subsys/usb/device/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/Kconfig)。

本仓库的[对应源码](../../../include/zephyr/usb/usb_device.h)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-device-support-deprecated"></a>
<a id="usb-device-stack"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="id5"></a>
<a id="id6"></a>
<a id="id7"></a>
<a id="id8"></a>
<a id="id9"></a>
<a id="id10"></a>
<a id="id11"></a>
<a id="id12"></a>
<a id="id13"></a>
<a id="id14"></a>
<a id="id15"></a>
<a id="id16"></a>
<a id="overview"></a>
<a id="supported-usb-classes"></a>
<a id="audio"></a>
<a id="bluetooth-hci-usb-transport-layer"></a>
<a id="cdc-acm"></a>
<a id="usb-device-cdc-acm"></a>
<a id="console-over-cdc-acm-uart"></a>
<a id="cdc-acm-uart-as-backend"></a>
<a id="posix-default-tty-echo-mitigation"></a>
<a id="dfu"></a>
<a id="usb-human-interface-devices-hid-support"></a>
<a id="mass-storage-class"></a>
<a id="networking"></a>
<a id="binary-device-object-store-bos-support"></a>
<a id="interface-number-and-endpoint-address-assignment"></a>
<a id="testing-over-usbip-in-native-sim"></a>
<a id="testing-usb-native-sim"></a>
<a id="usb-vendor-and-product-identifiers"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：USBC设备栈](P007_USBC设备栈.md) · [本模块主线目录](../reading/usb.md) · [全部主线](../reading/README.md) · [下一篇：USB设备API目录](P013_USB设备API目录.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P007_USBC设备栈.md) · [返回大纲](大纲.md) · [下一章](P009_USBC示例目录.md)

</details>

<!-- reading-navigation:end -->
