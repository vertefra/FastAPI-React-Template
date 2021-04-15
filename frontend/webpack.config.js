const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');

module.exports = {
	entry: './src/index.tsx',
	output: {
		filename: 'bundje.js',
		path: path.resolve(__dirname, 'dist'),
	},
	module: {
		rules: [
			{
				test: /\.tsx?$/,
				use: 'ts-loader',
				exclude: /node_modules/,
			},
			{
				test: /\.css$/i,
				use: ['style-loader', 'css-loader'],
			},
		],
	},
	resolve: {
		extensions: ['.ts', '.tsx', '.js', 'json'],
	},

	devServer: {
		contentBase: path.join(__dirname, 'dist'),
		host: '0.0.0.0',
		historyApiFallback: true,
		index: 'index.html',
		compress: true,
		hot: true,
		port: 9000,
	},
	plugins: [
		new HtmlWebpackPlugin({
			template: path.resolve(__dirname, 'src', 'index.html'),
		}),
	],

	optimization: {
		minimize: true,
		minimizer: [new CssMinimizerPlugin()],
	},
	devtool: 'source-map',
};
