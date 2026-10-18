---
id: learning.zephyr-docs.external_modules.page-5
title: Requests_HTTP客户端
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/requests.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="requests"></a>
<a id="external-module-requests"></a>

# 第5章\_Requests\_HTTP客户端

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/requests.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 5.1\_简介（Introduction）

<a id="id3"></a>

[requests](https://github.com/walidbadar/requests) 项目使用Zephyr网络协议栈，为GET、POST、PUT、DELETE等常见HTTP(S)操作提供易用接口。HTTP为超文本传输协议（Hypertext Transfer Protocol），HTTPS为其安全传输形式。项目还内置Zephyr Shell命令，可直接与HTTP(S)端点（Endpoint）交互。

```text
uart:~$ requests
requests - HTTP requests commands
Subcommands:
  get     : Perform HTTP GET request
            Usage: get <url>
  post    : Perform HTTP POST request
            Usage: post <url> <body>
  put     : Perform HTTP PUT request
            Usage: put <url> <body>
  delete  : Perform HTTP DELETE request
            Usage: delete <url>
uart:~$
```

> 译注——帮助对照：get执行HTTP GET请求，参数为url；post和put分别执行POST、PUT请求，参数为url及body，即请求正文；delete执行DELETE请求，参数为url。`uart:~$`是固件Shell提示符。这里的requests指下方所列Zephyr C项目，不能与同名Python HTTP库混同。

<a id="usage-with-zephyr"></a>

## 5.2\_在Zephyr中使用（Usage with Zephyr）

要引入requests模块，可在原文所称的 `west.yaml` 中添加west项目，或新建子清单，例如 `zephyr/submanifests/requests.yaml`，写入以下内容并运行 `west update`：

```yaml
manifest:
  projects:
    - name: requests
      url: https://github.com/walidbadar/requests.git
      revision: main
      path: modules/lib/requests # adjust the path as needed
```

API细节见requests头文件。原代码注释说明 `modules/lib/requests` 可按需要调整。

<a id="references"></a>

## 5.3\_参考资料（References）


<a id="id2"></a>

1. [requests项目仓库](https://github.com/walidbadar/requests)。


对应官方文档源码：[doc/develop/manifest/external/requests.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/requests.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/requests.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：LZ4压缩](P004_LZ4压缩.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：Memfault固件SDK](P006_Memfault固件SDK.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P004_LZ4压缩.md) · [返回大纲](大纲.md) · [下一章](P006_Memfault固件SDK.md)

</details>

<!-- reading-navigation:end -->
