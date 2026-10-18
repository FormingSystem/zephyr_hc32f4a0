---
id: learning.zephyr-docs.external_modules.page-11
title: wolfTPM
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/wolftpm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="wolftpm"></a>
<a id="external-module-wolftpm"></a>

# 第11章\_wolfTPM

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/wolftpm.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 11.1\_简介（Introduction）

wolfTPM是轻量、可移植的可信平台模块（Trusted Platform Module，TPM）2.0库，针对嵌入式系统、实时操作系统（Real-Time Operating System，RTOS）及资源受限设备优化。原文介绍它提供完整TPM 2.0实现，支持密码运算、密钥生成、安全存储和证明（Attestation）。

它已作为Zephyr模块集成，支持CMake和Kconfig，便于项目引入TPM功能。模块通过设备树支持与TPM设备的集成电路间总线（Inter-Integrated Circuit，I2C）通信：在 `user_settings.h` 将 `WOLFTPM_ZEPHYR_I2C_BUS` 设为描述设备I2C总线的节点，用 `WOLFTPM_ZEPHYR_I2C_SPEED` 配置速度。

wolfTPM采用GNU通用公共许可证第3版（GNU General Public License version 3，GPLv3）与商业许可证双重许可。

<a id="id2"></a>

GitHub仓库：[wolfTPM仓库](https://github.com/wolfSSL/wolfTPM)。

<a id="requirements"></a>

## 11.2\_要求（Requirements）

[wolfSSL](P008_wolfSSL.md#external-module-wolfssl)用于密码运算。

<a id="usage-with-zephyr"></a>

## 11.3\_在Zephyr中使用（Usage with Zephyr）

将wolfTPM作为项目加入自己的 `west.yml`：

```yaml
manifest:
  remotes:
  # <your other remotes>
  - name: wolftpm
    url-base: https://github.com/wolfssl
projects:
  # <your other projects>
  - name: wolftpm
    path: modules/crypto/wolftpm
    revision: v3.10.0
    remote: wolftpm
```

> 译注——原清单缩进：原块将 `projects:` 放在顶层，而west清单要求它属于 `manifest:`。使用前应把 `projects:` 及其所属项目列表整体右移两个空格，使 `projects:` 与 `remotes:` 对齐；上面的原块保持不变供对照。`<your other remotes>`／`<your other projects>`为保留其他远程来源／项目的注释，不是新建完整清单时可忽略现有配置的指令。依据见[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)的层级。

<a id="id3"></a>

**注意：**原修订号只是示例，请在 [wolfTPM仓库](https://github.com/wolfSSL/wolfTPM)的发行页面检查所需发布标签。

更新west模块：

```bash
west update
```

随后west会识别 `wolftpm` 模块，并把它的 `Kconfig` 和 `CMakeLists.txt` 接入构建系统。

<a id="sample-applications"></a>

## 11.4\_示例应用（Sample Applications）

wolfTPM包含两个Zephyr示例：

- `wolftpm_wrap_test`：测试TPM包装接口（Wrapper）的核心功能。
- `wolftpm_wrap_caps`：显示TPM能力（Capabilities）。

原文说明两例在 `qemu_x86` 上成功构建并运行，可作为开发起点。

> 译注：这是官方页面报告的结果，本批没有运行QEMU，也没有据此验证其他平台或物理TPM设备。

<a id="configuration"></a>

## 11.5\_配置（Configuration）

模块使用 `user_settings.h`，可按项目需求调整。与TPM设备进行I2C通信时配置：

- `WOLFTPM_ZEPHYR_I2C_BUS`：设为描述I2C总线的设备树节点。
- `WOLFTPM_ZEPHYR_I2C_SPEED`：设置I2C线路速度。

<a id="additional-resources"></a>

## 11.6\_补充资源（Additional Resources）

<a id="id5"></a>

<a id="id11"></a>

Zephyr用法见 [wolfTPM Zephyr示例说明](https://github.com/wolfSSL/wolfTPM/blob/master/zephyr/README.md)及 [wolfTPM Zephyr支持公告](https://www.wolfssl.com/wolftpm-support-for-zephyr-rtos/)。

<a id="id7"></a>

<a id="id9"></a>

Zephyr应用代码见 [wolfSSL NXP AppCodeHub](https://github.com/wolfSSL/nxp-appcodehub)；API说明见 [wolfTPM文档](https://www.wolfssl.com/documentation/manuals/wolftpm/)。

<a id="reference"></a>

## 11.7\_参考资料（Reference）


<a id="id1"></a>

1. [wolfTPM源码仓库](https://github.com/wolfSSL/wolfTPM)。

<a id="id4"></a>

2. [Zephyr示例说明](https://github.com/wolfSSL/wolfTPM/blob/master/zephyr/README.md)。

<a id="id6"></a>

3. [NXP应用代码集](https://github.com/wolfSSL/nxp-appcodehub)。

<a id="id8"></a>

4. [API文档](https://www.wolfssl.com/documentation/manuals/wolftpm/)。

<a id="id10"></a>

5. [Zephyr支持公告](https://www.wolfssl.com/wolftpm-support-for-zephyr-rtos/)。


对应官方文档源码：[doc/develop/manifest/external/wolftpm.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/wolftpm.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/wolftpm.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：wolfSSH](P010_wolfSSH.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：IEC60730_B类安全测试](P012_IEC60730_B类安全测试.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P010_wolfSSH.md) · [返回大纲](大纲.md) · [下一章](P012_IEC60730_B类安全测试.md)

</details>

<!-- reading-navigation:end -->
