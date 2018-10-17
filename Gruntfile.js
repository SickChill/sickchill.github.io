module.exports = function(grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        jsonlint: {
            files: ['scene_exceptions/scene_exceptions.json']
        },
        jshint: {
            files: ['Gruntfile.js']
        },
        watch: {
            files: ['<%= jsonlint.files %>', '<%=jshint.files %>'],
            tasks: ['jshint', 'jsonlint']
        },
        copy: {
            main: {
                files: [
                    {expand: true, cwd: 'node_modules/cryptofont/css', src: ['**'], dest: 'css', filter: 'isFile'},
                    {expand: true, cwd: 'node_modules/cryptofont/fonts', src: ['**'], dest: 'fonts', filter: 'isFile'},
                    {expand: true, cwd: 'node_modules/clipboard/dist', src: ['**.min.js'], dest: 'js', filter: 'isFile'},
                    // {expand: true, cwd: 'node_modules/bootstrap/dist/css', src: ['**.min.css'], dest: 'css', filter: 'isFile'},
                    // {expand: true, cwd: 'node_modules/bootstrap/dist/js', src: ['**.min.js'], dest: 'js', filter: 'isFile'},
                    // {expand: true, cwd: 'node_modules/bootstrap/dist/fonts', src: ['**'], dest: 'fonts', filter: 'isFile'},
                    {expand: true, cwd: 'node_modules/bootstrap-popover-x/css', src: ['**.min.css'], dest: 'css', filter: 'isFile'},
                    {expand: true, cwd: 'node_modules/bootstrap-popover-x/js', src: ['**.min.js'], dest: 'js', filter: 'isFile'},
                    // {expand: true, cwd: 'node_modules/jquery/dist', src: ['**.min.js'], dest: 'js', filter: 'isFile'},
                    {expand: true, cwd: 'node_modules/jquery.qrcode', src: ['**.min.js'], dest: 'js', filter: 'isFile'}
                ]
            }
        }
    });
    grunt.loadNpmTasks('grunt-jsonlint');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-copy');

    grunt.registerTask('test', ['jshint', 'jsonlint']);
    grunt.registerTask('default', ['jshint', 'jsonlint', 'copy']);


};
