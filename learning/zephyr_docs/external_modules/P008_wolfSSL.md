---
id: learning.zephyr-docs.external_modules.page-8
title: wolfSSL
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/wolfssl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="wolfssl"></a>
<a id="external-module-wolfssl"></a>

# 第8章\_wolfSSL

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/wolfssl.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 8.1\_简介（Introduction）

wolfSSL是轻量、可移植的安全套接层／传输层安全（Secure Sockets Layer / Transport Layer Security，SSL/TLS）库，针对嵌入式系统、实时操作系统（Real-Time Operating System，RTOS）及资源受限设备优化。它提供密码功能和安全通信协议，支持到TLS 1.3与数据报传输层安全（Datagram TLS，DTLS）1.3，并支持后量子密码学（Post-Quantum Cryptography）。多种构建配置使其适用于采用Zephyr的不同应用和硬件平台。

它支持Zephyr网络协议栈，应用可通过wolfSSL API与其他网络设备或服务建立安全连接。

wolfSSL采用GNU通用公共许可证第3版（GNU General Public License version 3，GPLv3）与商业许可证双重许可。

<a id="id2"></a>

GitHub仓库：[wolfSSL仓库](https://github.com/wolfSSL/wolfssl)。

<a id="usage-with-zephyr"></a>

## 8.2\_在Zephyr中使用（Usage with Zephyr）

将wolfSSL作为项目加入自己的 `west.yml`：

```yaml
manifest:
  remotes:
  # <your other remotes>
  - name: wolfssl
    url-base: https://github.com/wolfssl
projects:
  # <your other projects>
  - name: wolfssl
    path: modules/crypto/wolfssl
    revision: master
    remote: wolfssl
```

> 译注——原清单缩进：原块将 `projects:` 放在顶层，而west清单要求它属于 `manifest:`。使用前应把 `projects:` 及其所属项目列表整体右移两个空格，使 `projects:` 与 `remotes:` 对齐；上面的原块保持不变供对照。`<your other remotes>`／`<your other projects>`为保留其他远程来源／项目的注释，不是新建完整清单时可忽略现有配置的指令。依据见[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)的层级。

更新west模块：

```bash
west update
```

随后west会识别 `wolfssl` 模块，并把它的 `Kconfig` 和 `CMakeLists.txt` 接入构建系统。

<a id="id4"></a>

Zephyr用法见 [wolfSSL Zephyr示例说明](https://github.com/wolfSSL/wolfssl/blob/master/zephyr/README.md#build-and-run-wolfcrypt-benchmark-application)。

<a id="id6"></a>

<a id="id8"></a>

Zephyr应用代码见 [wolfSSL NXP AppCodeHub](https://github.com/wolfSSL/nxp-appcodehub)；API说明见 [wolfSSL文档](https://www.wolfssl.com/docs/)。

<a id="reference"></a>

## 8.3\_参考资料（Reference）


<a id="id1"></a>

1. [wolfSSL源码仓库](https://github.com/wolfSSL/wolfssl)。

<a id="id3"></a>

2. [Zephyr示例说明](https://github.com/wolfSSL/wolfssl/blob/master/zephyr/README.md#build-and-run-wolfcrypt-benchmark-application)。

<a id="id5"></a>

3. [NXP应用代码集](https://github.com/wolfSSL/nxp-appcodehub)。

<a id="id7"></a>

4. [API文档](https://www.wolfssl.com/docs/)。


对应官方文档源码：[doc/develop/manifest/external/wolfssl.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/wolfssl.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/wolfssl.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mender_MCU客户端](P007_Mender_MCU客户端.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：wolfMQTT](P009_wolfMQTT.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P007_Mender_MCU客户端.md) · [返回大纲](大纲.md) · [下一章](P009_wolfMQTT.md)

</details>

<!-- reading-navigation:end -->
