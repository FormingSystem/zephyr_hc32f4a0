---
id: learning.zephyr-docs.board-samples.page-34
title: Mesh多模型演示
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nordic/mesh/onoff_level_lighting_vnd_app/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nrf_bluetooth_mesh_onoff_level_lighting_vnd_app"></a>

# 第34章\_Mesh 多模型演示（Mesh Models）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nordic/mesh/onoff_level_lighting_vnd_app/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nordic/mesh/onoff_level_lighting_vnd_app/README.rst/..)

<a id="overview"></a>

## 34.1 概述（Overview）

本应用演示一个蓝牙 Mesh 节点，其根元素（Root element）包含以下模型：

> 译注——模型名称：Generic Level 表示可调的通用数值等级，不是网络层级；Default Transition Time 表示默认状态过渡时间；Power OnOff 描述上电后的开关行为；Light CTL 用于灯光亮度与色温等状态。Setup Server 提供对应设置状态的配置能力，不能因同名就当作另一个物理灯。

- 通用开关服务端（Generic OnOff Server）

- 通用开关客户端（Generic OnOff Client）

- 通用等级服务端（Generic Level Server）

- 通用等级客户端（Generic Level Client）

- 通用默认过渡时间服务端（Generic Default Transition Time Server）

- 通用默认过渡时间客户端（Generic Default Transition Time Client）

- 通用上电开关服务端（Generic Power OnOff Server）

- 通用上电开关设置服务端（Generic Power OnOff Setup Server）

- 通用上电开关客户端（Generic Power OnOff Client）

- 灯光亮度服务端（Light Lightness Server）

- 灯光亮度设置服务端（Light Lightness Setup Server）

- 灯光亮度客户端（Light Lightness Client）

- 灯光 CTL 服务端（Light CTL Server）

- 灯光 CTL 设置服务端（Light CTL Setup Server）

- 灯光 CTL 客户端（Light CTL Client）

- 厂商模型（Vendor Model）

次级元素（Secondary element）包含以下模型：

> 译注——模型清单与完整组成：本次 device_composition.c 显示两个元素；根元素还包含配置服务端与健康服务端等基础模型，并通过独立厂商模型数组加入 Vendor Model。原文上面的业务模型清单不是完整的 Composition Data 枚举。

- 通用等级服务端（Generic Level Server）

- 通用等级客户端（Generic Level Client）

- 灯光 CTL 色温服务端（Light CTL Temperature Server）

配网（Provisioning）之前，设备广播未配网信标（Unprovisioned beacon），其中包含唯一 UUID；该 UUID 来自 Nordic 在工厂信息配置寄存器（Factory Information Configuration Register，FICR）中设置的设备地址。

<a id="associations-of-models-with-hardware"></a>

## 34.2 模型与硬件的关联（Associations of Models with hardware）

nRF52840-PDK 开发板的模型关联关系如下：

- LED1 对应根元素中的通用开关服务端状态。

- LED2 对应根元素中的厂商模型。

- LED3 对应根元素的通用等级（Generic Level）／灯光实际亮度（Light Lightness Actual）值。

- LED4 对应次级元素的通用等级（Generic Level）／灯光 CTL 色温（Light CTL Temperature）值。

> 译注——LED 显示范围：本次 main.c 将亮度与色温换算为百分比，再用是否低于 50 的条件控制 LED3、LED4 的 GPIO。它们是状态指示，不是实际灯光的连续亮度／色温输出；LED2 则显示厂商模型的开关状态。

- Button1 与 Button2 对应根元素中的通用开关客户端或厂商模型。

- Button3 与 Button4 对应根元素中的通用等级客户端／灯光亮度客户端／灯光 CTL 客户端。

服务端状态之间按《Bluetooth SIG Mesh Model Specification v1.0》建立绑定关系（State binding）。

> 译注——两种绑定：这里 State binding 指不同模型状态之间的关联与换算，实现在 state_binding.c；后文 bind 命令把模型绑定到应用密钥，是另一种配置。原文引用规范 v1.0，保留其版本，不将本演示宣称为对后续全部规范功能的实现。

配网后，必须将按钮客户端配置为发布，将 LED 服务端配置为订阅。如果为服务端提供发布地址，它还会发布相应状态。

<a id="requirements"></a>

## 34.3 前提条件（Requirements）

原示例已在 Nordic nRF52840-PDK 开发板上测试，也可能在 nrf52dk/nrf52832 上运行。

<a id="building-and-running"></a>

## 34.4 构建与运行（Building and Running）

> 译注——执行前提：west 构建和烧录命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工具、模块、目标工具链与板卡；应用及配置为官方源码，构建目录由工具生成。构建成功后再烧录，出现错误先检查构建输出和板文档。后续 meshctl 命令属于独立的主机交互工具步骤。原文的板级测试结论不代表本次实测。

以下命令构建该应用。

```text
west build -b nrf52840dk/nrf52840 samples/boards/nordic/mesh/onoff_level_lighting_vnd_app
west flash
```

使用 BlueZ 的 meshctl 工具进行配网。本例将使用 meshctl 命令完成以下绑定：

> 译注——交互环境与命令范围：下方命令在 Linux 的 BlueZ meshctl 界面执行；主机须提供该工具与可用蓝牙适配器。target 0100 是本例根元素地址，1000／1001 为 Generic OnOff 服务端／客户端，1002／1003 为 Generic Level 服务端／客户端模型编号；bind 的元素索引 0 与单播地址 0100 不是同一种字段。该命令块只配置展示的 OnOff 与 Level 模型，没有配置清单里的全部灯光和厂商模型。

- 将 Button1、Button2 和 LED1 绑定到应用密钥 1，然后将 Button1、Button2 配置为向组地址 0xC000 发布，将 LED1 配置为订阅该组。

- 将 Button3、Button4 和 LED3 绑定到应用密钥 1，然后将 Button3、Button4 配置为向组地址 0xC000 发布，将 LED3 配置为订阅该组。

> 译注——默认按钮分支：本次 publisher.c 默认定义 ONOFF 与 GENERIC_LEVEL。其他 Lightness、CTL 或厂商消息分支由编译期宏选择，不是按任意按钮就自动轮换全部模型。更换分支时还需同步核对对应模型的应用密钥、发布地址与订阅。

```text
discover-unprovisioned on
provision <discovered UUID>
menu config
target 0100
appkey-add 1
bind 0 1 1000
bind 0 1 1001
bind 0 1 1002
bind 0 1 1003
sub-add 0100 c000 1000
sub-add 0100 c000 1002
pub-set 0100 c000 1 0 5 1001
pub-set 0100 c000 1 0 5 1003
```

meshctl 工具维护一个持久化 JSON 数据库，保存 Mesh 配置。随着更多节点（开发板）加入配网，它会根据节点支持的元素数量依次分配单播地址。本示例每个节点支持两个元素。

> 译注——网络状态：数据库中的密钥、节点地址与模型配置必须和实际设备匹配。正常重启工具可以复用已保存状态，不等于任意新数据库都能重新连接既有网络；不要把示例的网络索引 0x0 当成跨所有环境恒定的标识。

用于配置的 meshctl target 必须是根元素的单播地址，因为只有根元素具有配置服务端模型。正常退出 meshctl 后，可以重新启动它并重新连接网络 0x0。

meshctl 也支持开关模型客户端，可以改变绑定到应用密钥 0x1 的任意 LED 的状态。方法是将 target 设置为包含该 LED 模型的元素的单播地址，然后执行 onoff 命令。此处不支持组地址。

> 译注——限制归属：这里的组地址限制针对原文使用的 meshctl 客户端操作；Mesh 网络的组播发布／订阅仍按前面的 c000 配置工作。

本应用派生自 [samples/bluetooth/mesh](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/mesh) 中的 Mesh 示例骨架。

详情请参阅[蓝牙（Bluetooth）](../bluetooth_samples/P088_蓝牙示例总目录.md#bluetooth)示例。

<a id="see-also"></a>

## 34.5 另请参阅（See also）

[蓝牙 Mesh（Bluetooth Mesh）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html)

> 译注——源码入口：[main.c](../../../samples/boards/nordic/mesh/onoff_level_lighting_vnd_app/src/main.c)；[prj.conf](../../../samples/boards/nordic/mesh/onoff_level_lighting_vnd_app/prj.conf)；[device_composition.c](../../../samples/boards/nordic/mesh/onoff_level_lighting_vnd_app/src/mesh/device_composition.c)；[publisher.c](../../../samples/boards/nordic/mesh/onoff_level_lighting_vnd_app/src/mesh/publisher.c)；[state_binding.c](../../../samples/boards/nordic/mesh/onoff_level_lighting_vnd_app/src/mesh/state_binding.c)。这些相对链接用于查看本仓库参照实现，版本可能与本次官方页面不同。

对应官方文档源码：[samples/boards/nordic/mesh/onoff_level_lighting_vnd_app/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nordic/mesh/onoff_level_lighting_vnd_app/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nordic/mesh/onoff_level_lighting_vnd_app/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P033_Mesh开关模型.md) · [返回大纲](大纲.md) · [下一章](P035_Nordic示例目录.md)
