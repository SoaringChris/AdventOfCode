from enum import IntEnum
from math import prod
class PacketType(IntEnum):
    SUM = 0
    PRODUCT = 1
    MIN = 2
    MAX = 3
    LITERAL = 4
    GREATER = 5
    LESS = 6
    EQUAL = 7

def parseHex(data):
    return (bin(int(data, 16))[2:]).zfill(len(data) * 4)

def getPacketVersion(packet):
    return int(packet[:3], 2)

def getPacketType(packet):
    return int(packet[3:6], 2)

def parseLiteralPacket(packet):
    literalData = packet[6:]
    groups = [literalData[x : x + 5] for x in range(0, len(literalData), 5)]
    complete = False
    combined = ""
    remaining = ""
    for group in groups:
        if complete:
            remaining += group
        else:
            combined += group[1:]
        if(group[0] == '0'):
            complete = True
    return {'value': int(combined, 2), 'remaining': remaining}

def getLengthOfSubPackets(packet, size):
    return int(packet[7:7 + size], 2)

def parseOperatorPacket(packet):
    operatorType = getPacketType(packet)
    versionTotal = getPacketVersion(packet)
    sizeOfLength = 15 if packet[6:7] == "0" else 11
    lengthOfSubPackets = getLengthOfSubPackets(packet, sizeOfLength)
    terms = []
    if sizeOfLength == 15:
        subPackets = packet[7+sizeOfLength: 7 + sizeOfLength + lengthOfSubPackets]
        remaining = packet[7 + sizeOfLength + lengthOfSubPackets:]
        while len(subPackets) > 0 and len([x for x in subPackets if x != '0']) != 0:
            packetType = getPacketType(subPackets)
            if(packetType == PacketType.LITERAL):
                versionTotal += getPacketVersion(subPackets)
                result = parseLiteralPacket(subPackets)
                subPackets = result['remaining']
                terms.append(result['value'])
            else:
                result = parseOperatorPacket(subPackets)
                versionTotal += result['versionTotal']
                subPackets = result['remaining']
                terms.append(result['value'])
        value = 0
        match operatorType:
            case PacketType.SUM:
                value = sum(terms)
            case PacketType.PRODUCT:
                value = prod(terms)
            case PacketType.MIN:
                value = min(terms)
            case PacketType.MAX:
                value = max(terms)
            case PacketType.GREATER:
                value = 1 if terms[0] > terms[1] else 0
            case PacketType.LESS:
                value = 1 if terms[0] < terms[1] else 0
            case PacketType.EQUAL:
                value = 1 if terms[0] == terms[1] else 0
        return {
            'value': value,
            'versionTotal': versionTotal,
            'remaining': remaining
        }
    else:
        packetsFound = 0
        subPackets = packet[7 + sizeOfLength:]
        while packetsFound < lengthOfSubPackets:
            packetType = getPacketType(subPackets)
            if packetType == PacketType.LITERAL:
                versionTotal += getPacketVersion(subPackets)
                result = parseLiteralPacket(subPackets)
                subPackets = result['remaining']
                terms.append(result['value'])
            else:
                result = parseOperatorPacket(subPackets)
                versionTotal += result['versionTotal']
                subPackets = result['remaining']
                terms.append(result['value'])
            packetsFound += 1
        value = 0
        match operatorType:
            case PacketType.SUM:
                value = sum(terms)
            case PacketType.PRODUCT:
                value = prod(terms)
            case PacketType.MIN:
                value = min(terms)
            case PacketType.MAX:
                value = max(terms)
            case PacketType.GREATER:
                value = 1 if terms[0] > terms[1] else 0
            case PacketType.LESS:
                value = 1 if terms[0] < terms[1] else 0
            case PacketType.EQUAL:
                value = 1 if terms[0] == terms[1] else 0
        return{
            'value': value,
            'versionTotal': versionTotal,
            'remaining': subPackets
        }

        



input = open("input.txt", "r")

binary = parseHex(input.read())
if getPacketType(binary) == PacketType.LITERAL:
    print(getPacketVersion(binary)) #part1
    print(parseLiteralPacket(binary)['value']) #part2
else:
    value = parseOperatorPacket(binary)
    print(value['versionTotal']) #part1
    print(value['value']) #part2
