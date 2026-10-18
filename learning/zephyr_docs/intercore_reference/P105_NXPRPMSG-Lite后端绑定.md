---
id: learning.zephyr-docs.intercore_reference.ipcbind-105
title: NXPRPMSG-Lite后端绑定
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/ipc/nxp,ipc-rpmsg-lite.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第105章\_NXPRPMSG-Lite后端绑定

<a id="dtbinding-nxp-ipc-rpmsg-lite"></a>

原文：[nxp,ipc-rpmsg-lite](https://docs.zephyrproject.org/latest/build/dts/api/bindings/ipc/nxp,ipc-rpmsg-lite.html)。读取日期：2026-10-13，`latest`。

`nxp,ipc-rpmsg-lite`是 NXP Semiconductors 的设备树绑定（Devicetree Binding），用于处理器间通信（Inter-Processor Communication，IPC）。

此绑定描述通过邮箱信号通知（Mailbox-based Signaling）工作的 RPMsg-Lite IPC 服务后端（Backend）。RPMsg 指远程处理器消息传递（Remote Processor Messaging）；RPMsg-Lite 保留原组件名称。一个节点表示一条 RPMsg-Lite 链路（Link），也就是一个实例（Instance）。多条链路共用一个物理邮箱（Mailbox，MBOX）通道来发送处理器间通知。

通知拓扑（Signaling Topology）明确分为两种节点：`link-id = <0>`的实例拥有物理 MBOX 通道，声明标准的`mboxes`和`mbox-names`；其余实例通过`notification-parent`引用这个拥有者，并省略`mboxes`和`mbox-names`。

主机（Host）的`ipc[0,1]`分别通过匹配的`link-id`与远端（Remote）的`ipc[0,1]`通信。双方均共用一个物理 MBOX 通道，由未设置`notification-parent`的实例拥有，本例中即`link-id = <0>`的实例。

下文 TX 表示发送（Transmit），RX 表示接收（Receive）。

以下为主机侧（Host Side）原始设备树源码（Devicetree Source，DTS）示例：

```dts
/* Host side */
ipc0: ipc0 {
    compatible = "nxp,ipc-rpmsg-lite";
    memory-region = <&shm_ipc0>;
    mboxes = <&mbox 2>, <&mbox 3>;
    mbox-names = "tx", "rx";
    link-id = <0>;
    role = "host";
    status = "okay";
};

ipc1: ipc1 {
    compatible = "nxp,ipc-rpmsg-lite";
    memory-region = <&shm_ipc1>;
    notification-parent = <&ipc0>;
    link-id = <1>;
    role = "host";
    status = "okay";
};
```

以下为远端侧（Remote Side）示例；原注释要求链路标识必须与主机匹配，两个物理邮箱通道在两侧交换发送与接收角色：

```dts
/* Remote side -- link-id values must match the host */
ipc0: ipc0 {
    compatible = "nxp,ipc-rpmsg-lite";
    memory-region = <&shm_ipc0>;
    mboxes = <&mbox 3>, <&mbox 2>;
    mbox-names = "tx", "rx";
    link-id = <0>;
    role = "remote";
    status = "okay";
};

ipc1: ipc1 {
    compatible = "nxp,ipc-rpmsg-lite";
    memory-region = <&shm_ipc1>;
    notification-parent = <&ipc0>;
    link-id = <1>;
    role = "remote";
    status = "okay";
};
```

驱动为 [`subsys/ipc/ipc_service/backends/ipc_rpmsg_lite.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/ipc_rpmsg_lite.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,ipc-rpmsg-lite)。

属性类型中，`int`为整数，`array`为数值数组，`string`为字符串，`string-array`为字符串数组，`boolean`为布尔属性，`compound`为复合类型；`phandle`为节点引用（Phandle），`phandles`为节点引用列表，`phandle-array`为节点引用与说明单元数组。必需性和数值约束仅适用于所在层节点。

基础属性可用于多种节点，不保证全部适用于当前硬件。通用术语包括中断（Interrupt）、时钟（Clock）、电源域（Power Domain）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）和处理器间消息（Inter-Processor Messaging，IPM）。

## 105.1\_节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `role` | `string` | **必需**。本实例的 RPMSG-Lite 角色（Role）；`host`为主机，`remote`为远端；合法值：`host, remote` |
| `link-id` | `int` | **必需**。本实例的链路标识（Link ID），必须与远端对应实例匹配。允许范围为`[0 .. (DT_NUM_INST_STATUS_OKAY() - 1)]`；`DT_NUM_INST_STATUS_OKAY()`是统计已启用设备树实例数量的宏。`link-id = <0>`的实例必须通过`mboxes`和`mbox-names`拥有共享 MBOX 通道，其余实例必须通过`notification-parent`指向它 |
| `memory-region` | `phandle` | **必需**。引用此链路使用的共享内存区域（Shared Memory Region） |
| `notification-parent` | `phandle` | 引用同级的`nxp,ipc-rpmsg-lite`实例，该实例拥有共享 MBOX 通知通道，即`link-id = <0>`的实例。除直接声明`mboxes`和`mbox-names`的实例外，其余每个实例均应设置本属性。驱动借此避免重复注册 MBOX 回调（Callback），并把所有通知路由到同一物理通道 |
| `priority` | `array` | 各实例接收线程（RX Thread）的工作队列优先级（Work-queue Priority）。数组为`[priority, type]`，类型`PRIO_COOP`表示协作式（Cooperative）优先级，`PRIO_PREEMPT`表示抢占式（Preemptive）优先级；原始设置例子见表后。省略时默认采用`<0 PRIO_PREEMPT>` |
| `buffer-size` | `int` | 消息缓冲区的总字节数，包括16字节的 RPMSG-Lite 头部（Header）。应用可用的有效载荷（Payload）为`(buffer-size - 16)`字节。**主机与远端必须使用相同值，且该值必须大于16字节**。常见总大小与载荷大小：256→240字节，512→496字节（默认），1024→1008字节；默认值：`512` |
| `buffer-count` | `int` | 此链路发送／接收缓冲区（TX/RX Buffers）的数量。**必须是2的幂，主机与远端必须使用相同值**；默认值：`2` |
| `mboxes` | `phandle-array` | 引用用于处理器间通知的 MBOX 控制器通道；**恰好提供两个条目：发送（TX）和接收（RX）**。只有`link-id = <0>`的通知拥有者（Notification Owner）声明本属性，其余实例使用`notification-parent` |
| `mbox-names` | `string-array` | MBOX 通道名称必须是`tx`和`rx`，顺序必须与`mboxes`中的条目对应 |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg` | `array` | 给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md) |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
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
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁（Hardware Spinlock）标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |
| `zephyr,deferred-init` | `boolean` | 延迟初始化（Deferred Initialization）：启动时不自动初始化设备，应由应用使用 `device_init()` 手动初始化 |
| `wakeup-source` | `boolean` | 标记设备可用作唤醒源（Wakeup Source）。设置该属性后，设备中会设置专门标志，通知系统此设备有唤醒能力。唤醒功能默认禁用，即中断不会唤醒系统；必要时可在运行期间启用 |
| `zephyr,pm-device-runtime-auto` | `boolean` | 初始化函数执行后，自动为设备配置运行时电源管理（Runtime Power Management） |
| `zephyr,disabling-power-states` | `phandles` | 会关闭该设备电源的电源状态（Power State）列表 |

工作队列优先级的原例保留如下；注释中的`K_PRIO_COOP(1)`和`K_PRIO_PREEMPT(2)`分别是协作式、抢占式线程优先级宏：

```dts
  priority = <1 PRIO_COOP>;    /* K_PRIO_COOP(1)    */
  priority = <2 PRIO_PREEMPT>; /* K_PRIO_PREEMPT(2) */
```

`reg-names`的原例说明寄存器块（Register Block）命名；`uart`为通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）节点名。

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

`uart@1000`有两个寄存器块：名称为`foo`的块基址为`0x1000`、大小为`0x2000`；名称为`bar`的块基址为`0x3000`、大小为`0x4000`。

本页没有已弃用的顶层专用属性。

服务使用方式见 [IPC 服务使用指南](P092_IPC服务使用指南.md)。

---

[上一章：NordicnRF本地IPCT绑定](P104_NordicnRF本地IPCT绑定.md) · [下一章：ZephyrICBMsg后端绑定](P106_ZephyrICBMsg后端绑定.md) · [返回大纲](大纲.md)
