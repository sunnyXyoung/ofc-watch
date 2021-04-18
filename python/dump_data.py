import re


def dump_castle_damage(report_list):
    castle_damage = {}
    for report in report_list:
        for message in report['report']['messages']['messages']:
            if message['m'][-3:] == '點傷害':
                p = re.compile(r'\d+')
                if message['m'][:len(report['report']['aName'])] == report['report']['aName']:
                    if not report['report']['bName']:
                        castle_damage[report['report']['aName']] = castle_damage.get(report['report']['aName'],
                                                                                     0) + int(
                            p.findall(message['m'])[-1])
    return castle_damage


def dump_damage(report_list):
    damage = {}
    for report in report_list:
        for message in report['report']['messages']['messages']:
            if message['m'][-3:] == '點傷害':
                p = re.compile(r'\d+')
                if message['m'][:len(report['report']['aName'])] == report['report']['aName']:
                    if report['report']['bName']:
                        damage[report['report']['aName']] = damage.get(report['report']['aName'], 0) + int(
                            p.findall(message['m'])[-1])
                else:
                    damage[report['report']['bName']] = damage.get(report['report']['bName'], 0) + int(
                        p.findall(message['m'])[-1])
    return damage


def dump_damaged(report_list):
    damaged = {}
    for report in report_list:
        for message in report['report']['messages']['messages']:

            if message['m'][-3:] == '點傷害':
                p = re.compile(r'\d+')

                if message['m'][:len(report['report']['aName'])] == report['report']['aName']:
                    if report['report']['bName']:
                        damaged[report['report']['bName']] = damaged.get(report['report']['bName'], 0) + int(
                            p.findall(message['m'])[-1])
                else:
                    damaged[report['report']['aName']] = damaged.get(report['report']['aName'], 0) + int(
                        p.findall(message['m'])[-1])
    return damaged


def dump_faction12(report_list):
    factions = []
    for report in report_list:
        if report['report']['aFactionName'] not in factions: factions.append(
            report['report']['aFactionName'])
        if report['report']['bFactionName'] not in factions: factions.append(
            report['report']['bFactionName'])
    return factions


def dump_faction1(report_list):
    faction_damage = {}
    for report in report_list:
        for message in report['report']['messages']['messages']:
            if message['m'][-3:] == '點傷害':
                p = re.compile(r'\d+')
                if message['m'][:len(report['report']['aName'])] == report['report']['aName']:
                    if report['report']['bName']:
                        faction_damage[report['report']['aFactionName']] = faction_damage.get(
                            report['report']['aFactionName'], 0) + int(p.findall(message['m'])[-1])
                else:
                    faction_damage[report['report']['bFactionName']] = faction_damage.get(
                        report['report']['bFactionName'], 0) + int(p.findall(message['m'])[-1])


def dump_faction2(report_list):
    pass
