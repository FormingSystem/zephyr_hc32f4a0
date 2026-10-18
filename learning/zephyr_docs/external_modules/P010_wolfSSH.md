---
id: learning.zephyr-docs.external_modules.page-10
title: wolfSSH
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/wolfssh.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="wolfssh"></a>
<a id="external-module-wolfssh"></a>

# 第10章\_wolfSSH

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/wolfssh.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 10.1\_简介（Introduction）

wolfSSH是轻量、可移植的安全Shell（Secure Shell，SSH）库，针对嵌入式系统、实时操作系统（Real-Time Operating System，RTOS）及资源受限设备优化。它提供SSH服务端和客户端实现，支持安全复制（Secure Copy，SCP）及SSH文件传输协议（SSH File Transfer Protocol，SFTP）；多种构建配置适合采用Zephyr的不同应用与硬件平台。

它支持Zephyr网络协议栈，应用可通过wolfSSH API与其他网络设备或服务建立安全SSH连接。

wolfSSH采用GNU通用公共许可证第3版（GNU General Public License version 3，GPLv3）与商业许可证双重许可。

<a id="id2"></a>

GitHub仓库：[wolfSSH仓库](https://github.com/wolfSSL/wolfssh)。

<a id="requirements"></a>

## 10.2\_要求（Requirements）

[wolfSSL](P008_wolfSSL.md#external-module-wolfssl)用于密码运算。

<a id="usage-with-zephyr"></a>

## 10.3\_在Zephyr中使用（Usage with Zephyr）

将wolfSSH作为项目加入自己的 `west.yml`：

```yaml
manifest:
  remotes:
  # <your other remotes>
  - name: wolfssh
    url-base: https://github.com/wolfssl
projects:
  # <your other projects>
  - name: wolfssh
    path: modules/lib/wolfssh
    revision: master
    remote: wolfssh
```

> 译注——原清单缩进：原块将 `projects:` 放在顶层，而west清单要求它属于 `manifest:`。使用前应把 `projects:` 及其所属项目列表整体右移两个空格，使 `projects:` 与 `remotes:` 对齐；上面的原块保持不变供对照。`<your other remotes>`／`<your other projects>`为保留其他远程来源／项目的注释，不是新建完整清单时可忽略现有配置的指令。依据见[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)的层级。

更新west模块：

```bash
west update
```

随后west会识别 `wolfssh` 模块，并把它的 `Kconfig` 和 `CMakeLists.txt` 接入构建系统。

<a id="id4"></a>

Zephyr用法见 [wolfSSH Zephyr示例说明](https://github.com/wolfSSL/wolfssh/blob/master/zephyr/README.md#build-and-run-samples)。

<a id="id6"></a>

<a id="id8"></a>

Zephyr应用代码见 [wolfSSL NXP AppCodeHub](https://github.com/wolfSSL/nxp-appcodehub)；API说明见 [wolfSSH文档](https://www.wolfssl.com/documentation/manuals/wolfssh/)。

<a id="reference"></a>

## 10.4\_参考资料（Reference）


<a id="id1"></a>

1. [wolfSSH源码仓库](https://github.com/wolfSSL/wolfssh)。

<a id="id3"></a>

2. [Zephyr示例说明](https://github.com/wolfSSL/wolfssh/blob/master/zephyr/README.md#build-and-run-samples)。

<a id="id5"></a>

3. [NXP应用代码集](https://github.com/wolfSSL/nxp-appcodehub)。

<a id="id7"></a>

4. [API文档](https://www.wolfssl.com/documentation/manuals/wolfssh/)。


对应官方文档源码：[doc/develop/manifest/external/wolfssh.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/wolfssh.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/wolfssh.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：wolfMQTT](P009_wolfMQTT.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：wolfTPM](P011_wolfTPM.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P009_wolfMQTT.md) · [返回大纲](大纲.md) · [下一章](P011_wolfTPM.md)

</details>

<!-- reading-navigation:end -->
