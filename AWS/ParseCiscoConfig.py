def parse_cisco_configuration(data):
    data = data.split('\n')
    print(data)
    subnets = []
    current_interface = None
    description = None
    for line in data:
        line = line.lower().strip()

        if 'interface ' in line:
            current_interface = line.lstrip('interface').strip()
        if 'ip address' in line and current_interface:
            line_segments = line.split(' ')
            if not len(line_segments) in [4, 5]:
                continue
            else:
                subnets.append(
                    {
                        'ip': line_segments[2],
                        'mask': line_segments[3],
                        'is_secondary': line_segments[-1] == 'secondary',
                        'interface': current_interface,
                    }
                )

    print(subnets)

    return subnets