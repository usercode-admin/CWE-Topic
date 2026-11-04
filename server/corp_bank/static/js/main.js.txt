$(document).ready(function() {
    var updateClock = function() {
        var now = new Date();
        $('#datetime').text(now.toUTCString());
    };
    updateClock();
    setInterval(updateClock, 1000);

    $('.panel').hide().fadeIn(600);

    if (window.location.pathname.includes('infrastructure')) {
        function loadSystemMetrics() {
            $.getJSON('/api/system_info', function(data) {
                $('#sys-os').text(data.os_sys);
                $('#sys-hostname').text(data.hostname);
                $('#sys-cpu').text(data.arch + ' (' + data.cpu_count + ' Cores)');
                $('#sys-disk-detail').text(data.disk_used + ' / ' + data.disk_total + ' (Free: ' + data.disk_free + ')');
                $('#sys-ram-detail').text(data.ram_used + ' / ' + data.ram_total);
                $('#sys-uptime').text(data.uptime);
                $('#sys-pyver').text('Python v' + data.python_ver);

                $('#sys-ram-text').text(data.ram_percent + '% (' + data.ram_used + ')');
                $('#sys-ram-bar').css('width', data.ram_percent + '%');

                $('#sys-disk-text').text(data.disk_percent + '% (' + data.disk_used + ')');
                $('#sys-disk-bar').css('width', data.disk_percent + '%');
            });
        }
        loadSystemMetrics();
        setInterval(loadSystemMetrics, 5000);
    }
});
