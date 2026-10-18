---
id: learning.zephyr-docs.networking.page-155
title: TTCN3协议一致性测试
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/conformance/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第155章\_TTCN3协议一致性测试

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/conformance/index.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. TTCN-3 协议一致性测试（Protocol Conformance Testing）

Zephyr 从两个方向测试网络协议。[tests/net](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net) 下的测试使用 C 编写，与被测实现编译进同一映像，从内部检验实现。TTCN-3 一致性测试套件（Conformance Suite）则从外部入手：通过真实网络接口与 Zephyr 交互，把它发出的内容与标准要求进行比较。

两类测试能发现不同问题。针对实现编写的测试容易把实现当前的行为写成预期；针对标准编写的套件不需要知道实现内部如何工作，这正是它的价值。

TTCN-3 是欧洲电信标准化协会（European Telecommunications Standards Institute，ETSI）标准化的测试编写语言。本组套件使用开源 TTCN-3 编译器 [Eclipse Titan](https://projects.eclipse.org/projects/tools.titan) 编译，保存在 net-tools 仓库的 `ttcn3` 下，与其他主机端网络测试工具放在一起。

- 操作方法：[运行一致性测试套件](P157_运行协议一致性测试.md)。
- 组成与扩展方法：[一致性测试的架构](P156_一致性测试架构.md)。

> 术语译注：TTCN-3 全称为测试与测试控制表示法第 3 版（Testing and Test Control Notation Version 3），见 [ETSI 官方介绍](https://ttcn-3.etsi.org/index.php/about/introduction)。

## 2. 各部分如何配合（How It Fits Together）

一致性测试的 Zephyr 侧只是被测系统（System Under Test，SUT）：一个启用了待测协议的普通应用。测试逻辑不会编译进它，没有控制通道（Control Channel）；套件完全通过网络驱动它。

这些应用以及对它们运行套件的测试控制层（Test Harness），位于 [tests/net/conformance](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance)。Twister 构建并启动应用，一个小型 pytest 控制层使用 Titan 构建套件、运行套件，再把 Titan 判定（Verdict）转换为测试结果。

如果缺少 Titan、第三方 TTCN-3 模块或网络接口，各测试会自行跳过（Skip），因此不会让未准备这些条件的常规测试运行失败。所需条件见运行指南，组件关系见架构页。

## 3. 测试套件（The Suites）

套件使用的接口及是否必须以 root 运行，由它的测试内容决定：工作在 IP 层以下的套件，使用独立链路上的包套接字（Packet Socket）读取帧。

| 套件（Suite） | 被测系统（System Under Test） | 接口（Interface） | 运行身份（Runs As） |
| --- | --- | --- | --- |
| [mdns](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/mdns/README.rst) | [tests/net/conformance/mdns](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/mdns) | `zeth` | 任意用户 |
| [dnssd](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/dnssd/README.rst) | [tests/net/conformance/dnssd](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/dnssd) | `zeth` | 任意用户 |
| [dns](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/dns/README.rst) | [tests/net/conformance/dns](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/dns) | `zeth` | 任意用户 |
| [sntp](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/sntp/README.rst) | [tests/net/conformance/sntp](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/sntp) | `zeth` | 任意用户 |
| [mqtt](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/mqtt/README.rst) | [tests/net/conformance/mqtt](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/mqtt) | `zeth` | 任意用户 |
| [coap](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/coap/README.rst) | [tests/net/conformance/coap](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/coap) | `zeth` | 任意用户 |
| [dhcpv4](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/dhcpv4/README.rst) | [tests/net/conformance/dhcpv4](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/dhcpv4) | `zeth` | `root` |
| [dhcpv4_server](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/dhcpv4_server/README.rst) | [tests/net/conformance/dhcpv4_server](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/dhcpv4_server) | `zeth` | `root` |
| [arp](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/arp/README.rst) | [tests/net/conformance/arp](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/arp) | `zethL2` | `root` |
| [ndp](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/ndp/README.rst) | [tests/net/conformance/ndp](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/ndp) | `zethL2` | `root` |
| [tcp](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/tcp/README.rst) | [tests/net/conformance/tcp](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/tcp) | `zethL2` | `root` |

新增套件的方法见 [添加测试套件](P156_一致性测试架构.md#ttcn3-adding-a-suite)。

## 4. 已知覆盖缺口（Known Gaps）

如果套件断言的行为与标准不一致，会在断言位置明确说明，把差异记录下来，避免悄然将其固化。以下是另一类缺口：目前尚无套件覆盖的部分。

### 4.1 DNS-SD 传统单播查询（Legacy Unicast Queries）

多播 DNS（Multicast DNS，mDNS）响应器的主机名部分，按照 [RFC 6762](https://datatracker.ietf.org/doc/html/rfc6762.html) 第 6.7 节回答传统单播查询。但 DNS 服务发现（DNS-Based Service Discovery，DNS-SD）部分不这样做：它自行构造消息，为属于同一实例的记录设置缓存清除位（Cache-Flush Bit），采用原本用于多播应答的生存期，并且既不回显标识符，也不回显问题。修正它需要重新处理名称压缩偏移（Name Compression Offset），因为这些偏移目前都从固定首部长度算起。

[`dnssd`](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/dnssd/README.rst) 套件在 `f_check_legacy_shape` 中记录这一行为，而不是断言标准要求，以免测试在实现修复前一直失败。那里每项检查均说明未来需要同步修改的内容。

### 4.2 MQTT 5.0、包标识符与重发（Packet Identifiers and Re-Sending）

[`mqtt`](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/mqtt/README.rst) 套件覆盖 MQTT 3.1.1。Zephyr 也实现了 MQTT 5.0（[`CONFIG_MQTT_VERSION_5_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MQTT_VERSION_5_0)），但 Titan 项目没有发布相应协议模块；要覆盖它，需先编写消息类型，再编写测试。

包标识符与重发也未覆盖。Zephyr 客户端把这两项交给应用管理：[`mqtt_publish()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga57745efa1bf6fbdf7eb1b3f01623e4c7) 使用传入的标识符与重复标志（Duplicate Flag）发送。因此测试这些内容，实际测到的会是被测应用自己的计数器，而不是 MQTT 客户端库。

### 4.3 重叠的 DNS 查询（Overlapping DNS Queries）

解析器向一个没有未完成请求的服务端发送查询前，会更新源端口（Source Port）。默认同一时间只有一个查询，因此每次查询都会更新。对同一服务端重叠进行的查询仍共享端口，[`dns`](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/dns/README.rst) 套件中的检查无法发现这种情况下的回归。参见 [RFC 5452](https://datatracker.ietf.org/doc/html/rfc5452.html) 第 9.2 节。

## 5. 持续集成（Continuous Integration）

这些套件不属于普通 Twister 运行：它们需要 Titan 安装、面向设备的网络接口以及套件源码检出，而普通构建不具备这些条件。它们运行较慢，并且不能彼此同时运行。

它们改由 [.github/workflows/net_conformance.yml](https://github.com/zephyrproject-rtos/zephyr/blob/main/.github/workflows/net_conformance.yml) 每夜运行；也可从 GitHub Actions 页手动启动。拉取请求（Pull Request）修改测试、运行脚本或工作流本身时，也会触发。作业使用 GitHub 托管虚拟机，而非容器，因为创建 TAP 接口需要 `CAP_NET_ADMIN`，项目自有运行器的容器不具备该能力。

作业安装发行版打包的 Titan，然后运行 [scripts/net/run-conformance-tests.sh](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/net/run-conformance-tests.sh)。脚本创建两个接口，以 `sudo` 运行整个测试目录，避免因权限不足而跳过套件。作业设置 `NET_CONFORMANCE_REQUIRED`，使不能运行的套件判失败而非跳过：没有实际测试任何内容的运行，不应看起来像测试通过。Twister 报告和控制层日志作为产物（Artifacts）保存。

> 译注：此处描述的是官方测试工作流；本次只翻译和核对源码，没有创建、修改或执行任何定时任务。

## 6. 其他 TTCN-3 套件（Other TTCN-3 Suites）

Eclipse Titan 项目在 [gitlab.eclipse.org/eclipse/titan](https://gitlab.eclipse.org/eclipse/titan) 下的多个独立仓库发布协议模块（Protocol Module）和测试端口（Test Port）。这里的套件基于这些模块构建，不自行重新定义消息格式。

那里也有一些完整套件。`titan.misc` 包含 CoAP 一致性套件，可针对 [CoAP 服务示例](P072_CoAP服务示例.md#coap-server)运行；该用法见 [CoAP](P064_CoAP协议库.md#coap-sock-interface) 文档。

Intel 曾在 TCP 重写期间编写一个较早的 TTCN-3 TCP 套件，它为现在 [`tcp`](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance/tcp/README.rst) 套件的覆盖范围提供了参考，但这里没有复用其代码。旧套件通过 JSON 控制通道驱动 Zephyr，并断言协议栈内部状态名称；该通道需要的配置选项已经移除，见官方 4.5 迁移指南。


<a id="protocol-conformance-testing-with-ttcn-3"></a>
<a id="ttcn3-testing"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="id5"></a>
<a id="id6"></a>
<a id="id7"></a>
<a id="id8"></a>
<a id="how-it-fits-together"></a>
<a id="the-suites"></a>
<a id="ttcn3-suites"></a>
<a id="known-gaps"></a>
<a id="ttcn3-known-gaps"></a>
<a id="dns-sd-legacy-unicast-queries"></a>
<a id="index-0"></a>
<a id="mqtt-5-0-packet-identifiers-and-re-sending"></a>
<a id="overlapping-dns-queries"></a>
<a id="index-1"></a>
<a id="continuous-integration"></a>
<a id="other-ttcn-3-suites"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：网络跟踪](P154_网络跟踪.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：一致性测试架构](P156_一致性测试架构.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P154_网络跟踪.md) · [返回大纲](大纲.md) · [下一章](P156_一致性测试架构.md)

</details>

<!-- reading-navigation:end -->
