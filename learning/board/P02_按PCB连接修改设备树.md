---
id: learning-board-2
title: 按 PCB 连接修改设备树
kind: tutorial
status: ready
domains: [embedded, tools]
---
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 2. 按 PCB 连接修改设备树

## 2.1 先从电路事实走到软件描述

[上一章](P01_选择目标板与软件配置.md)选定了 board/SoC。本章讨论同一芯片换 PCB 接线后改什么。设备树（devicetree）描述硬件节点、地址和连接；驱动读取生成数据并初始化硬件。描述能解析只说明语法与约束通过，不等于驱动实现了任意接线。

先从原理图建立表：器件信号→芯片物理脚号→GPIO 端口/位号→复用功能→电气要求。物理封装脚号不是 tx-pin 或 GPIO 索引；例如 PA9 表示 A 端口第 9 位，不能填成芯片第 9 脚。

本板装 HC32F4A0PITB，采用 12 MHz 晶振。封装缺失引脚按 NC；不能根据兼容芯片原理图启用不存在的脚。适配前还应核对供电、上下拉、有效电平、SWD/启动脚占用。具体核实依据留在[硬件记录](../../project-docs/hardware.md)。

## 2.2 DTS、DTSI、overlay 和 binding

DTS 是 Devicetree Source（设备树源码）；DTSI 是设备树源码的包含文件（Devicetree Source Include）扩展名约定。
overlay 是叠加在基础树上的修改文件；binding 是约束节点属性的规则文件。它们共同生成供驱动使用的数据。

| 名称 | 作用 | 当前例子 |
| --- | --- | --- |
| .dtsi | 可复用芯片描述，被板文件包含 | dts/arm/xhsc/hc32f4a0pitb.dtsi |
| 板 .dts | 整块板的默认硬件连接 | boards/uyup/uyup_rpi_a/uyup_rpi_a_hc32f4a0pitb.dts |
| overlay | 针对一次应用构建叠加修改 | learning/board/labs/green-led.overlay |
| binding | 规定节点属性类型、必需项与允许值 | dts/bindings/serial/xhsc,hc32-uart.yaml |
| 驱动 | 真正访问寄存器的实现 | drivers/serial/uart_hc32.c |

节点标签供其他节点引用；`&green_led` 表示引用已定义标签，`aliases` 给应用提供约定名称；`chosen` 指定控制台等系统用途。`status = "okay"` 启用节点，还需软件驱动被 Kconfig/CMake 纳入。

长期同一 PCB 的公共接线通常归板 .dts；一个应用的可选外设配置适合 overlay；芯片外设寄存器和封装限制放芯片描述层。实际发布新 PCB 型号时建立独立板身份更利于追踪，不长期把完全不同的板伪装成原板。

## 2.3 不猜新引脚，先切换已存在的 LED

原板 blue_led 是 PD10，green_led 是 PE15，均为低有效。应用使用 led0 别名。本章 overlay 只改别名：

```dts
/ {
    aliases {
        led0 = &green_led;
    };
};
```

沿用上一章的 pcb-green 构建命令，再查看生成结果：

```bash
rg -n -A 7 "aliases|green_led|blue_led" build/learning-tools/pcb-green/zephyr/zephyr.dts
```

预期 led0 引用 green_led 对应的节点。应用源码仍使用 led0，因此按此固件在真实板上运行时应操作绿灯；本轮只验证合并设备树和编译，未烧录观察灯。

修改挑战：另存一个 overlay 切回 blue_led，使用另一个 -B 目录比较生成 zephyr.dts。不要编辑原板文件做一次性的实验，也不要把生成的 zephyr.dts 改动当作输入。

## 2.4 真正换引脚应该怎样写

支持 GPIO 的板上，节点里的 gpios 通常由控制器引用、控制器内引脚编号和标志构成。改 PCB 时，要一起核对引用的端口、位号、GPIO_ACTIVE_LOW/HIGH、外部上拉及应用的逻辑有效含义。确认原理图后才修改板 .dts 或应用 overlay；本教程不提供未经核实的替代脚号。

UART、SPI 等复用外设更进一步。许多 SoC 使用 pinctrl（引脚复用状态）描述一组引脚，但其写法依赖该 SoC 的 binding、宏和驱动。先找同一 SoC 已工作的例子及驱动支持，不能把另一芯片的 pinctrl 宏直接复制过来。[官方设备树操作指南](https://docs.zephyrproject.org/latest/build/dts/howtos.html)

## 2.5 当前 HC32 UART 的明确限制

当前 USART1 是 PA9 TX、PA10 RX。[UART binding](../../dts/bindings/serial/xhsc,hc32-uart.yaml)允许引脚索引 0..15，但 [uart_hc32.c](../../drivers/serial/uart_hc32.c)仍限定实例及这组端口/引脚，不匹配时返回 -ENOTSUP；底层复用功能也按当前组合设置。

因此合法地把 tx-pin 改成另一个 0..15 数字，可能通过设备树生成和编译，运行时驱动仍拒绝初始化。当前不存在“编辑一份 HC32 pinctrl 文件即可任意换 UART 引脚”的实现。

真正增加受支持映射，需要核对芯片手册的复用表、封装可用脚和 PCB，修改驱动的配置处理/约束，必要时扩展 binding 或实现 pinctrl，然后补构建与实板收发测试。不要删掉约束让错误配置静默通过。

故意用越界索引观察更早一层的失败：

```bash
python scripts/project_env.py exec cmake -S samples/bringup -B build/learning-tools/pcb-invalid -G Ninja -DBOARD=uyup_rpi_a/hc32f4a0pitb -DDTC_OVERLAY_FILE=../../learning/board/labs/invalid-uart.overlay
```

预期在配置阶段因 tx-pin=16 不在 binding 枚举中失败；这是实验预期。恢复时使用正确 overlay 或独立目录，不要修改 binding 放宽范围来“修复”越界测试。

## 2.6 适配完成需要什么证据

依次核对原理图与封装、最终 zephyr.dts、最终 .config、驱动实现与编译结果、实板电平与收发行为。时钟、Flash 等待周期和供电变化也属于板级工程，不能因为 GPIO 示例编译通过就认定整板已适配。

清理仅涉及 pcb-green、pcb-invalid 等本章产物。完成标志是能解释“语法合法”“驱动支持”“硬件接线正确”三个不同判断。[下一章：Twister 与 QEMU](P03_用Twister和QEMU验证配置.md)。
