"""Rebuild reading routes from the official page inventory, without counting new translations."""
# SPDX-License-Identifier: Apache-2.0
from collections import defaultdict
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
BASIC_SAMPLES = {'samples/basic/blinky/README.html', 'samples/hello_world/README.html'}
ORDER = 'getting_started toolchains developer_tools west application build_system cmake_reference kconfig devicetree sysbuild snippets modules external_modules llext api_guides hardware kernel memory_services smf languages portability debugging testing twister sca optimizations storage power usb networking bluetooth interaction observability io_services modbus data_utilities dsp crypto tfm serialization sensors firmware_update intercore_reference'.split()


def is_guide(record):
    return record['path'] in BASIC_SAMPLES or (
        record['path'] != 'kconfig.html'
        and record['category'] not in {'doxygen', 'samples', 'boards', 'snippets'}
        and not record['path'].startswith(('build/dts/api/bindings/', 'build/dts/api/compatibles/'))
    )


def title(path):
    text = path.read_text(encoding='utf-8')
    match = re.search(r'^title: (.+)$', text, re.M)
    return match[1] if match else path.stem


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text(encoding='utf-8') != text:
        path.write_text(text, encoding='utf-8')


def document(identifier, heading, body):
    return f'---\nid: learning.zephyr-docs.{identifier}\ntitle: {heading}\nkind: reference\nstatus: evolving\ndomains: [zephyr, documentation]\n---\n\n<!-- SPDX-License-Identifier: Apache-2.0 -->\n\n# {heading}\n\n{body.rstrip()}\n'


def main():
    records = json.loads((ROOT / 'inventory.json').read_text(encoding='utf-8'))['records']
    translated = [r for r in records if r['status'] == 'translated']
    guides = defaultdict(list)
    references = defaultdict(list)
    for record in translated:
        if is_guide(record):
            guides[record['translation'].split('/')[0]].append(record)
        else:
            category = record['category']
            kind = 'kconfig' if record['path'] == 'kconfig.html' else 'bindings' if record['path'].startswith(('build/dts/api/bindings/', 'build/dts/api/compatibles/')) else category
            references[kind].append(record)
    count = sum(map(len, guides.values()))
    modules = sorted(guides, key=lambda m: (ORDER.index(m) if m in ORDER else len(ORDER), m))
    overview = [f'这里按学习顺序列出已翻译的 {count} 个官方指南页面，包含入门所需的 Blinky 和 Hello World。其他示例、开发板、具体绑定和自动生成 API 单独收在[官方扩展参考](../reference_library/README.md)。页面内由官方正文引用的参考链接仍可正常打开。',
                '章节编号沿用原册；阅读顺序以本目录及页尾“主线阅读”导航为准。源码跟踪与技术纠错译注保留；仓库源码链接使用相对路径。',
                '| 阅读模块 | 已译页面 |\n| --- | ---: |']
    for module in modules:
        rows = sorted(guides[module], key=lambda r: r['translation'])
        heading = title(ROOT / module / '大纲.md').replace('大纲', '').strip(' ：')
        overview.append(f'| [{heading}]({module}.md) | {len(rows)} |')
        listing = [f'本目录只列官方指南正文。编号可能不连续；其他条目可在[扩展参考](../reference_library/README.md)查阅。\n\n[返回官方主线目录](README.md)\n']
        for index, row in enumerate(rows):
            path = ROOT / row['translation']
            label = title(path)
            listing.append(f'- [{label}](../{row["translation"]})')
            text = path.read_text(encoding='utf-8')
            marker = '<!-- reading-navigation:start -->'
            if marker in text:
                before, old = text.split(marker, 1)
                match = re.search(r'<summary>原册编号导航（含扩展参考）</summary>\n\n(.*?)\n\n</details>', old, re.S)
                if not match:
                    raise ValueError(f'Cannot recover original navigation: {path.name}')
                original = match[1]
            else:
                match = re.search(r'\n(\[(?:上一|下一|返回|后续|前置)[^\n]+)\s*$', text)
                if not match:
                    raise ValueError(f'Cannot identify navigation: {path.name}')
                before = text[:match.start()].rstrip() + '\n\n'
                original = match[1]
            links = []
            if index:
                previous = rows[index - 1]
                links.append(f'[上一篇：{title(ROOT / previous["translation"])}]({Path(previous["translation"]).name})')
            links.append(f'[本模块主线目录](../reading/{module}.md)')
            links.append('[全部主线](../reading/README.md)')
            if index + 1 < len(rows):
                following = rows[index + 1]
                links.append(f'[下一篇：{title(ROOT / following["translation"])}]({Path(following["translation"]).name})')
            navigation = ' · '.join(links)
            write(path, before + marker + '\n\n**主线阅读**\n\n' + navigation + '\n\n<details>\n<summary>原册编号导航（含扩展参考）</summary>\n\n' + original + '\n\n</details>\n\n<!-- reading-navigation:end -->\n')
        write(ROOT / 'reading' / f'{module}.md', document(f'reading.{module}', heading + ' · 官方主线', '\n'.join(listing)))
    overview.extend(['', '[翻译集首页](../README.md) · [搜索全部官方页面](../catalog.html) · [全站进度](../PROGRESS.md)'])
    write(ROOT / 'reading/README.md', document('reading.readme', 'Zephyr 官方主线阅读', '\n\n'.join(overview[:2]) + '\n\n' + '\n'.join(overview[2:])))
    reference_labels = {'bindings': '设备树绑定（Devicetree Bindings）', 'doxygen': '自动生成 API、结构体与源码参考', 'samples': '示例（Samples）', 'boards': '开发板与扩展板（Boards and Shields）', 'snippets': '具体配置片段（Snippets）', 'kconfig': 'Kconfig 配置项完整参考'}
    overview = [f'已翻译的 {len(translated) - count} 个官方参考页面按用途单独收录，查型号、接口或示例时从这里进入。它们仍属于 Zephyr 官网文档；原有正文、图片和动图保留原位，旧链接继续有效。',
                '[返回官方主线阅读](../reading/README.md) · [搜索全部官方页面](../catalog.html)\n',
                '| 参考分类 | 已译页面 |\n| --- | ---: |']
    for kind in reference_labels:
        rows = sorted(references.get(kind, []), key=lambda r: r['path'])
        if not rows:
            continue
        heading = reference_labels[kind]
        overview.append(f'| [{heading}]({kind}.md) | {len(rows)} |')
        listing = ['[返回扩展参考目录](README.md) · [官方主线阅读](../reading/README.md)\n']
        for row in rows:
            listing.append(f'- [{title(ROOT / row["translation"])}](../{row["translation"]}) — `{row["path"]}`')
        write(ROOT / 'reference_library' / f'{kind}.md', document(f'reference-library.{kind}', heading, '\n'.join(listing)))
    assert sum(map(len, references.values())) + count == len(translated)
    assert set(references) <= set(reference_labels)
    kconfig_coverage = ROOT / 'kconfig_reference/coverage.json'
    if kconfig_coverage.is_file():
        coverage = json.loads(kconfig_coverage.read_text(encoding='utf-8'))
        overview.append(
            '\n[Kconfig 配置项完整参考](../kconfig_reference/大纲.md)：'
            f'已完成 {coverage["translated_records"]}/{coverage["records_total"]} 条定义记录。'
            + ('全部定义已译完，按源码模块分为 ' + str(coverage['translated_chapters']) + ' 章；全站清单按一个官方动态页面计数。'
             if references.get('kconfig') else '按逐条正文推进，整页完成状态仍以全站清单为准。'))
    media_pending = [r for r in records if r.get('text_status') == 'translated' and r['status'] == 'pending']
    if media_pending:
        overview.append(
            '\n另有 ' + str(len(media_pending)) + ' 页正文已译完，但原始图片文件仍有缺项，未计入上面的完整完成数。'
            '可从[缺失媒体清单与译文入口](../MISSING_MEDIA.md)阅读，缺项和原地址逐项保留。')
    write(ROOT / 'reference_library/README.md', document('reference-library.readme', 'Zephyr 官方扩展参考', '\n\n'.join(overview[:1]) + '\n\n' + '\n'.join(overview[1:])))
    progress_path = ROOT / 'PROGRESS.md'
    progress = progress_path.read_text(encoding='utf-8')
    progress = re.sub(
        r'\[官方主线\]\(reading/README.md\)包含\d+个已译页面；\[扩展参考\]\(reference_library/README.md\)包含\d+个已译页面，包括[^。]+。',
        f'[官方主线](reading/README.md)包含{count}个已译页面；[扩展参考](reference_library/README.md)包含{len(translated)-count}个已译页面，包括'
        + '、'.join(f'{len(references.get(key, []))}页{label}' for key, label in [('bindings', '绑定'), ('doxygen', '自动生成参考'), ('samples', '示例'), ('boards', '开发板'), ('snippets', '具体配置片段'), ('kconfig', 'Kconfig完整参考')] if references.get(key)) + '。',
        progress,
    )
    write(progress_path, progress)
    print(json.dumps({'translated': len(translated), 'guides': count, 'references': {k: len(v) for k, v in references.items()}, 'guide_modules': len(guides)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
