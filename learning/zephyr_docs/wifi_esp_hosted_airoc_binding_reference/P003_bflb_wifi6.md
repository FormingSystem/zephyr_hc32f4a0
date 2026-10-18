---
id: learning.zephyr-docs.wifi-esp-hosted-airoc-binding-reference.page-3
title: bflb_wifi6
kind: reference
status: maintained
domains: [zephyr, devicetree, wifi]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/wifi/bflb,wifi6.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第3章\_bflb_wifi6

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/wifi/bflb,wifi6.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="bflb-wifi6"></a>
<a id="dtbinding-bflb-wifi6"></a>
<a id="std-dtcompatible-bflb-wifi6"></a>

兼容字符串（Compatible String）：`bflb,wifi6`。厂商：[ Bouffalo Lab (Nanjing) Co., Ltd. ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-bflb)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=bflb,wifi6)。

驱动源码（Driver Source）：[drivers/wifi/bflb/wifi6/bflb_wifi_net.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/wifi6/bflb_wifi_net.c)。

<a id="description"></a>

Bouffalo Lab WiFi6介质访问控制器（Wi-Fi MAC）。

这是较新BFLB芯片BL61x、BL616CL、BL618DG采用的CEVA-Waves IP二进制固件与硬件组合，具有Wi-Fi、低功耗蓝牙（BLE）、IEEE 802.15.4，以及可选的经典蓝牙／增强数据率（BT/EDR）功能。

译注术语：HT为高吞吐量（High Throughput），VHT为甚高吞吐量（Very High Throughput），HE为高效率（High Efficiency），MCS为调制与编码方案（Modulation and Coding Scheme）；数字20、40、80、160表示相应信道带宽。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 3.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pwr-table-11b` | `array` | 802.11b各速率（1、2、5.5、11 Mbps）的发射功率目标（TX Power Target），共4项，单位为四分之一dBm。 |
| `pwr-table-11g` | `array` | 802.11g各速率（6～54 Mbps）的发射功率目标（TX Power Target），共8项。 |
| `pwr-table-11n-ht20` | `array` | 802.11n HT20模式MCS 0～7的发射功率目标（TX Power Target），共8项。 |
| `pwr-table-11n-ht40` | `array` | 802.11n HT40模式MCS 0～7的发射功率目标（TX Power Target），共8项。 |
| `pwr-table-11ac-vht20` | `array` | 802.11ac VHT20模式MCS 0～9的发射功率目标（TX Power Target），共10项。 |
| `pwr-table-11ac-vht40` | `array` | 802.11ac VHT40模式MCS 0～9的发射功率目标（TX Power Target），共10项。 |
| `pwr-table-11ax-he20` | `array` | 802.11ax HE20模式MCS 0～11的发射功率目标（TX Power Target），共12项。 |
| `pwr-table-11ax-he40` | `array` | 802.11ax HE40模式MCS 0～11的发射功率目标（TX Power Target），共12项。 |
| `pwr-table-11ac-vht80` | `array` | 802.11ac VHT80模式MCS 0～9的发射功率目标（TX Power Target），共10项。 |
| `pwr-table-11ax-he80` | `array` | 802.11ax HE80模式MCS 0～11的发射功率目标（TX Power Target），共12项。 |
| `pwr-table-11ax-he160` | `array` | 802.11ax HE160模式MCS 0～11的发射功率目标（TX Power Target），共12项。 |
| `pwr-offset` | `array` | 信道1～14逐信道发射功率偏移（Per-Channel TX Power Offset），共14项。采用原始类型－长度－值编码（Type-Length-Value，TLV）：值16表示0 dBm偏移，每一步为0.25 dBm。 |
| `pwr-offset-lp` | `array` | 信道1～14逐信道低功耗发射功率偏移（Low-Power TX Power Offset），共14项，编码与 `pwr-offset` 相同。 |
| `xtal-capcode-in` | `int` | 晶体输入引脚的负载电容编码（Crystal Load Capacitor Code），范围0～63。；范围：`0 to 63` |
| `xtal-capcode-out` | `int` | 晶体输出引脚的负载电容编码（Crystal Load Capacitor Code），范围0～63。；范围：`0 to 63` |
| `tcal-enable` | `boolean` | 启用温度校准（Temperature Calibration）。 |
| `tcal-linear-or-follow` | `int` | 温度校准模式（Temperature Calibration Mode）：0为线性模式（Linear），1为跟随模式（Follow）。；范围：`0 to 1` |
| `tcal-channels` | `array` | 温度校准信道频率（Calibration Channel Frequencies），共5项，单位MHz。 |
| `tcal-channel-os` | `array` | 温度校准信道偏移（Calibration Channel Offsets），共5项，为有符号值，但按 `uint16` 编码。 |
| `tcal-channel-os-low` | `array` | 低功耗模式的温度校准信道偏移（Low-Power Calibration Channel Offsets），共5项，为有符号值，但按 `uint16` 编码。 |
| `tcal-troom-os` | `int` | 温度校准室温偏移（Room Offset），编码256表示0，255表示−1，257表示+1。；范围：`0 to 512` |
| `tcap-enable` | `boolean` | 启用电容编码温度补偿（Capcode Temperature Compensation）。 |
| `tcap-tsen` | `array` | 电容编码温度补偿所用的传感器值（Sensor Values），共10项。 |
| `tcap-capcode` | `array` | 电容编码温度补偿所用的电容编码值（Capcode Values），共11项。 |

本页没有已弃用的节点专用属性。

## 3.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `interrupts` | `array` | **必需**。Wi-Fi MAC与IPC中断，共2项：`wifi` 对应MAC，`wifi-ipc` 对应IPC。 |
| `interrupt-names` | `string-array` | **必需**。设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg` | `array` | 给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的名称；通用说明称其为可选名称，是否必须填写以本层的必需标记为准 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节 |
| `dma-coherent` | `boolean` | 表示设备支持一致性 DMA 操作，见规范 v0.4 第 2.3.10 节 |
| `dmas` | `phandle-array` | 与设备相关的 DMA 通道说明符 |
| `dma-names` | `string-array` | `dmas` 中各 DMA 通道说明符的可选名称 |
| `dma-ranges` | `compound` | 定义总线物理地址空间与其父总线物理地址空间之间的映射或转换，见规范 v0.4 第 2.3.9 节 |
| `io-channels` | `phandle-array` | 与设备相关的 I/O 通道说明符 |
| `io-channel-names` | `string-array` | `io-channels` 中各通道说明符的可选名称 |
| `mboxes` | `phandle-array` | 与设备相关的邮箱/IPM 通道说明符 |
| `mbox-names` | `string-array` | `mboxes` 中各邮箱说明符的可选名称 |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁（Hardware Spinlock）标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |
| `zephyr,deferred-init` | `boolean` | 延迟初始化（Deferred Initialization）：启动时不自动初始化设备，应由应用使用 `device_init()` 手动初始化 |
| `wakeup-source` | `boolean` | 标记设备可用作唤醒源（Wakeup Source）。设置该属性后，设备中会设置专门标志，通知系统此设备有唤醒能力。唤醒功能默认禁用，即中断不会唤醒系统；必要时可在运行期间启用 |
| `zephyr,pm-device-runtime-auto` | `boolean` | 初始化函数执行后，自动为设备配置运行时电源管理（Runtime Power Management） |
| `zephyr,disabling-power-states` | `phandles` | 会关闭该设备电源的电源状态（Power State）列表 |

属性说明中的“重要属性”参见[设备树语法与结构](../devicetree/P003_语法与结构.md#dt-important-props)。

## 3.3\_寄存器块命名原例

以下设备树源码（Devicetree Source，DTS）演示 `reg-names` 命名；`uart` 指通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）。

```dts
  / {
       soc {
           #address-cells = <1>;
           #size-cells = <1>;

           uart@1000 {
               reg = <0x1000 0x2000>, <0x3000 0x4000>;
               reg-names = "foo", "bar";
           };
       };
  };
```

`uart@1000` 节点有两个寄存器块（Register Block）：一个基址为 `0x1000`、大小为 `0x2000`、名称为 `foo`；另一个基址为 `0x3000`、大小为 `0x4000`、名称为 `bar`。

---

[上一章](P002_bflb_wifi4.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_espressif_esp-at.md)
