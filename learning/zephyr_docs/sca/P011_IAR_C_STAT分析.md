---
id: learning.zephyr-docs.sca.sca-iar_c_stat
title: IAR_C_STAT分析
kind: reference
status: maintained
domains: [zephyr, sca]
source_url: https://docs.zephyrproject.org/latest/develop/sca/iar_c_stat.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第11章\_IAR_C_STAT分析

原文：[IAR C-STAT support](https://docs.zephyrproject.org/latest/develop/sca/iar_c_stat.html)。读取日期：2026-10-12，`latest`。

[IAR C-STAT](https://iar.com/cstat) 是面向 C/C++ 源码的综合静态分析工具，可发现错误和漏洞，支持 MISRA C、MISRA C++、CERT C/C++ 与 CWE 等规则体系。

> 译注：**汽车工业软件可靠性协会（Motor Industry Software Reliability Association，MISRA）**在此指其编码规范；CERT 是安全编码规范名称，CWE 是**通用弱点枚举（Common Weakness Enumeration）**，用于分类软件弱点。C-STAT 是 IAR 产品名，不将它拆成杜撰的英文全称。

## 11.1\_安装条件

C-STAT 随 IAR Build Tools 和 IAR Embedded Workbench 预装，安装细节按所用产品文档检查。

## 11.2\_构建时运行

运行该接入需要 **CMake 4.1.0 或更高版本**。调用 `west build` 时追加选择参数 `-DZEPHYR_SCA_VARIANT=iar_c_stat`：

```sh
west build -b stm32f429ii_aca samples/basic/blinky -- -DZEPHYR_SCA_VARIANT=iar_c_stat
```

> 译注：在已具备目标工具链、依赖与 IAR 工具的 Zephyr 源码根，用 Bash 执行。`stm32f429ii_aca` 是官方示例板目标；选择分析器的参数不等于自动安装 IAR，也不能单凭这一参数推断所有板都受支持。配置失败时先核对 CMake 版本与工具发现结果。本次没有运行分析。

## 11.3\_自定义分析选项

下表参数既可由 CMake 命令行提供，也可作为环境变量设置：

| 参数 | 含义 |
| --- | --- |
| `CSTAT_RULESET` | 预定义规则集，默认 `stdchecks`；允许 `all,cert,misrac2004,misrac2012,misrac++2008,stdchecks,security`。 |
| `CSTAT_ANALYZE_THREADS` | 分析线程数，默认主机处理器数。 |
| `CSTAT_ANALYZE_OPTS` | 直接传给 `analyze` 命令的参数，例如 `--timeout=900;--deterministic;--fpe`。 |
| `CSTAT_DB` | 覆盖 C-STAT 使用的 SQLite 数据库位置，可指向自选的 `cstat.db` 文件。 |
| `CSTAT_CLEANUP` | 清理该 SQLite 数据库，例如设为 `true`。 |

SQLite 是保存分析数据所用的数据库实现名。`stdchecks` 为默认检查集标识，`all` 为全部规则集合标识，其余项分别选择安全或对应年份的规范；实际支持情况以当前工具为准。

下面示例组合 MISRA C 2012 与 CERT 规则：

```sh
# From the root of the zephyr repository
west build -b stm32f429ii_aca samples/basic/blinky -- -DZEPHYR_SCA_VARIANT=iar_c_stat -DCSTAT_RULESET=misrac2012,cert
```

> 译注：规则集使用逗号组合，与 `CSTAT_ANALYZE_OPTS` 的分号参数列表不同。原文数据库路径用固定用户目录举例，本译文改为不绑定机器位置的文件名说明，实际传入值仍须按工具要求解析到可写位置。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：ECLAIR分析](P010_ECLAIR分析.md) · [本模块主线目录](../reading/sca.md) · [全部主线](../reading/README.md) · [下一篇：Polyspace分析](P012_Polyspace分析.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：ECLAIR分析](P010_ECLAIR分析.md) · [返回大纲](大纲.md) · [下一章：Polyspace分析](P012_Polyspace分析.md)

</details>

<!-- reading-navigation:end -->
